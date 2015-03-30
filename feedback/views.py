from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

def index(request):
    return redirect('ask')

def ask(request):
    return render_to_response('ask.html', RequestContext(request))

def give(request):
    return render_to_response('give.html', RequestContext(request))
