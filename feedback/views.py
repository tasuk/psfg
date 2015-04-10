from django.shortcuts import render, redirect

from .models import Questionnaire, Feedback
from .services import send_feedback_creation_email

def index(request):
    return redirect('ask')

def ask(request):
    if request.method == 'POST':
        questionnaire = Questionnaire().create(
            request.POST['asker_email'],
            request.POST['asker_name'],
        )

        questionnaire.save()
        send_feedback_creation_email(request, questionnaire)

        return render(request, 'create.html', {
            'form_url': request.build_absolute_uri(questionnaire.get_url()),
        })

    return render(request, 'ask.html', {
        'workagain_options': Feedback.workagain_options,
    })

def give(request, public_id):
    questionnaire = Questionnaire.objects.get(public_id=public_id)

    if request.method == 'POST':
        feedback = Feedback()
        feedback.questionnaire = questionnaire
        feedback.workagain = request.POST['workagain']
        feedback.didenjoy = request.POST['didenjoy']
        feedback.didnotenjoy = request.POST['didnotenjoy']
        feedback.save()

        return redirect('thanks')

    return render(request, 'give.html', {
        'questionnaire': questionnaire,
        'workagain_options': Feedback.workagain_options,
    })

def thanks(request):
    return render(request, 'thanks.html')

def review(request, public_id, token):
    # exception on invalid token
    questionnaire = Questionnaire.objects.get(public_id=public_id, token=token)
    feedbacks = Feedback.objects.filter(questionnaire=questionnaire)

    return render(request, 'review.html', {
        'feedbacks': feedbacks,
        'form_url': request.build_absolute_uri(questionnaire.get_url()),
    })
