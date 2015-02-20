from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)

class Questionnaire(models.Model):
    name = models.CharField(max_length=200)

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    question_type = models.CharField(max_length=1, choices=(
        ('t', 'text'),
        ('c', 'choice'),
        ('m', 'multichoice'),
    ))
    mandatory = models.BooleanField()

class Feedback(models.Model):
    creator = models.ForeignKey(User)
    answerer = models.ForeignKey(User)
    questionnaire = models.ForeignKey(Questionnaire)

class Answer(models.Model):
    feedback = models.ForeignKey(Feedback)
    answer = models.CharField(max_length=200)
