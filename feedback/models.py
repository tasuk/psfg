import mandrill, random

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.template import loader

# This is an utter abomination, but hey, we're prototyping!

def create_identifier(length):
    def get_random(string):
        return random.SystemRandom().choice(string)

    return ''.join(
        get_random('bcdfghjklmnpqrstvwxz') + get_random('aeiouy')
        for _ in range(int(length / 2))
    )

class Questionnaire(models.Model):
    public_id = models.CharField(max_length=10, unique=True)
    token = models.CharField(max_length=20)
    name = models.CharField(max_length=100, blank=True)
    asker_email = models.CharField(max_length=200)
    asker_name = models.CharField(max_length=200)

    def create(asker_email, asker_name):
        return Questionnaire(
            public_id=create_identifier(8),
            token=create_identifier(20),
            asker_email=asker_email,
            asker_name=asker_name,
        )

    def __str__(self):
        return "%s (%s)" % (self.name, self.public_id)

    def get_url(self):
        return reverse('give', kwargs={'public_id': self.public_id})

    def get_admin_url(self):
        return reverse('review', kwargs={'public_id': self.public_id, 'token': self.token})

    def send_admin_link(self, request):
        mandrill_client = mandrill.Mandrill(settings.MANDRILL_API_KEY)
        mandrill_client.messages.send({
            'from_email': 'info@peopleskillsforgeeks.com',
            'from_name': 'People Skills For Geeks',
            'subject': 'Feedback Form',
            'html': loader.render_to_string('emails/admin_link.html', {
                'asker_name': self.asker_name,
                'form_url': request.build_absolute_uri(self.get_url()),
                'form_admin_url': request.build_absolute_uri(self.get_admin_url()),
            }),
            'auto_text': True,
            'to': [{
                'email': self.asker_email,
                'name': self.asker_name,
            }],
            'track_clicks': False,
            'track_opens': False,
        })

class Feedback(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    giver_name = models.CharField(max_length=200, blank=True)
    workagain = models.IntegerField()
    didenjoy = models.TextField(blank=True)
    didnotenjoy = models.TextField(blank=True)

    def __str__(self):
        return "For %s (%s); %s (%i)" % (
            self.questionnaire.name,
            self.questionnaire.public_id,
            self.giver_name,
            self.id,
        )
