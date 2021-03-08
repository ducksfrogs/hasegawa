#from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello World. You are at the index of oil.")

def detail(request, question_id):
    return HttpResponse("You are at question %s." % question_id)

def results(request, question_id):
    response = "You are lokking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
