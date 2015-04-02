import random
from django.shortcuts import render, redirect
from .models import Questionnaire, Feedback

def index(request):
    return redirect('ask')

def ask(request):
    def get_identifier():
        def get_random(string):
            return random.SystemRandom().choice(string)

        return ''.join(
            get_random('bcdfghjklmnpqrstvwxz') + get_random('aeiouy')
            for _ in range(4)
        )

    if request.method == 'POST':
        questionnaire = Questionnaire(
            public_id=get_identifier(),
            asker_email=request.POST['asker_email'],
            asker_name=request.POST['asker_name'],
        )
        questionnaire.save()

        return render(request, 'create.html', {
            'form_url': request.build_absolute_uri(questionnaire.get_url()),
        })

    return render(request, 'ask.html')

def give(request):
    return render(request, 'give.html')
