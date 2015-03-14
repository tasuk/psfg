from django.shortcuts import redirect, render_to_response

def index(request):
    return render_to_response('index.html')

def mail(request):
    return redirect('http://eepurl.com/bcn2t5', True)
