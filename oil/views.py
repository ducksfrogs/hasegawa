#from django.http import Http404
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
#from django.template import loader
from django.shortcuts import render

from .models import Question


def index(request):

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'oil/index.html', context)

def detail(request, question_id):
#    try:
#        question = Question.objects(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'oil/detail.html', {'question': question})
#
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'oil/detail.html', {'question': question})

def results(request, question_id):
    response = "You are lokking at the results of question %s"
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)
