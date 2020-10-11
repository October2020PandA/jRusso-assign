from django.shortcuts import render, redirect, HttpResponse
from logreg.models import User
from questionCreator.models import QuestionType, Question, QuestionGroup, QuestionChoice
from .models import Answer, CompleteGroup

# Create your views here.
def testerHome(request):
    context = {
        'title': 'Create a new Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'question_groups': QuestionGroup.objects.filter(complete_groups__in=CompleteGroup.objects.filter(user=User.objects.get(id=request.session['login_id']), is_completed=0)),
        'completed_groups': QuestionGroup.objects.filter(complete_groups__in=CompleteGroup.objects.filter(user=User.objects.get(id=request.session['login_id']), is_completed=1)),
    } 
    return render(request, 'question_list.html', context)

def takeTest(request, tid):
    context = {
        'title': 'Create a new Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'questions': Question.objects.filter(question_group=QuestionGroup.objects.get(id=tid)).all(),
    } 
    return render(request, 'question_take.html', context)

def reviewTest(request, tid):
    context = {
        'title': 'Create a new Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'questions': Question.objects.filter(question_group=QuestionGroup.objects.get(id=tid)).all(),
        'answers': Answer.objects.filter(question_group=QuestionGroup.objects.get(id=tid), user=User.objects.get(id=request.session['login_id'])),
    } 
    return render(request, 'review_group.html', context)

def submitTest(request, tid):
    user_data = User.objects.get(id=request.session['login_id'])
    q_group = QuestionGroup.objects.get(id=tid)
    for key, value in request.POST.items():
        if key[0:6] == 'answer':
            question_data = Question.objects.get(id=key[7:len(key)])
            Answer.objects.create(user=user_data, question_group=q_group, question=question_data, answer=value)
    c_group = CompleteGroup.objects.get(user=user_data, question_group=q_group)
    c_group.is_completed=1
    c_group.save()
    return redirect('/')