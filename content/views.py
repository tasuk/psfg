from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

def mail(request):
    return redirect('http://eepurl.com/bcn2t5')

def meetup(request):
    return redirect('http://www.meetup.com/People-Skills-for-Geeks')
