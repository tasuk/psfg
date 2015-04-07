import random

from django.core.urlresolvers import reverse
from django.db import models

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

    def create(self, asker_email, asker_name):
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

class Feedback(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    giver_name = models.CharField(max_length=200, blank=True)
    workagain = models.IntegerField()
    didenjoy = models.TextField(blank=True)
    didnotenjoy = models.TextField(blank=True)

    workagain_options = {
        1: {"give": "I'd rather be quartered", "review": "They'd rather be quartered"},
        2: {"give": "I'd rather not", "review": "They'd rather not"},
        3: {"give": "I wouldn't mind", "review": "They wouldn't mind"},
        4: {"give": "I'd be happy to", "review": "They'd be happy to"},
        5: {"give": "Very much so", "review": "Very much so"},
        6: {"give": "More than anything", "review": "More than anything"},
    }

    def __str__(self):
        return "For %s (%s); %s (%i)" % (
            self.questionnaire.name,
            self.questionnaire.public_id,
            self.giver_name,
            self.id,
        )

    def get_workagain_choice(self):
        return self.workagain_options[self.workagain]['review']
