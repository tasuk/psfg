from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

def index(request):
    return redirect('/labs')

def labs(request):
    return render_to_response('index.html', RequestContext(request))

def mail(request):
    return redirect('http://eepurl.com/bcn2t5', True)
