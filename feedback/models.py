from django.db import models

class User(models.Model):
    email = models.CharField(max_length=200)

class Questionnaire(models.Model):
    name = models.CharField(max_length=200)

class Question(models.Model):
    TEXT = 't'
    CHOICE = 'c'

    questionnaire = models.ForeignKey(Questionnaire)
    label = models.CharField(max_length=200)
    question_type = models.CharField(max_length=1, choices=(
        (TEXT, 'text'),
        (CHOICE, 'choice'),
    ))
    mandatory = models.BooleanField(default=False)
    order = models.IntegerField()

class Option(models.Model):
    question = models.ForeignKey(Question)
    name = models.CharField(max_length=200)
    label = models.CharField(max_length=200)
    order = models.IntegerField()

class Feedback(models.Model):
    questionnaire = models.ForeignKey(Questionnaire)
    creator = models.ForeignKey(User, related_name='feedback_creator')
    answerer = models.ForeignKey(User, related_name='feedback_answerer')

class Answer(models.Model):
    feedback = models.ForeignKey(Feedback)
    answer = models.CharField(max_length=200)
