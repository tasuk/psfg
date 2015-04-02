from django.core.urlresolvers import reverse
from django.db import models

# This is an utter abomination, but hey, we're prototyping!

class Questionnaire(models.Model):
    public_id = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=100, blank=True)
    asker_email = models.CharField(max_length=200)
    asker_name = models.CharField(max_length=200)

    def __str__(self):
        return "%s (%s)" % (self.name, self.public_id)

    def get_url(self):
        return reverse('give', kwargs={'public_id': self.public_id})

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
