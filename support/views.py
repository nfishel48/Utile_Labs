from django.shortcuts import render, render_to_response
from django.http import HttpResponse

def index(request, option):
    return render_to_response('support/index.html', {'option': option + '.html'})
