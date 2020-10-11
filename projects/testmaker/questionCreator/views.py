from django.shortcuts import render, redirect, HttpResponse
from logreg.models import User
from .models import QuestionType, Question, QuestionGroup, QuestionChoice
from questionTaker.models import CompleteGroup

# Create your views here.
def question(request):
    context = {
        'title': 'Create a new Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'question_groups': QuestionGroup.objects.filter(user=User.objects.get(id=request.session['login_id'])),
    } 
    return render(request, 'question.html', context)

def qg_form(request):
    context = {
        'title': 'Create a new Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
    } 
    return render(request, 'question_group.html', context)

def qg_view(request, qgid):
    context = {
        'title': 'Question Group',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'questions': Question.objects.filter(question_group=QuestionGroup.objects.get(id=qgid)),
        'question_group': qgid,
    } 
    return render(request, 'view_question_group.html', context)

def q_form(request, qgid):
    context = {
        'title': 'Create a new Question',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'question_types': QuestionType.objects.all(),
    } 
    return render(request, 'question_creation.html', context)

def q_create(request, qgid):
    if request.method == 'POST':
        Question.objects.create(question=request.POST['id_question'], answer=request.POST['id_answer'], question_type=QuestionType.objects.get(id=request.POST['id_question_type']) , question_group=QuestionGroup.objects.get(id=qgid))
    return redirect('..')

def q_read(request, qgid, qid):
    return HttpResponse('q_read')

def q_update(request, qgid, qid):
    return HttpResponse('q_update')

def q_delete(request, qgid, qid):
    return HttpResponse('q_delete')

def qg_create(request):
    QuestionGroup.objects.create(group_name=request.POST['id_group_name'], user=User.objects.get(id=request.session['login_id'])) 
    return redirect('1/')

def qg_read(request, qgid):
    return HttpResponse('qg_read')

def qg_update(request, qgid):
    return HttpResponse('qg_update')

def qg_delete(request, qgid):
    return HttpResponse('qg_delete')

def qg_testers(request, qgid):
    context = {
        'title': 'Add Testers',
        'first_name': User.objects.get(id=request.session['login_id']).first_name,
        'question_group': qgid,
        'testers': QuestionGroup.objects.get(id=qgid).complete_groups.all(),
        'users': User.objects.exclude(id__in=QuestionGroup.objects.get(id=qgid).complete_groups.all().values_list('id', flat=True)),
    } 
    return render(request, 'add_tester.html', context)

def qg_testerAdd(request, qgid):
    q_group = QuestionGroup.objects.get(id=qgid)
    user_data = User.objects.get(id=request.session['login_id'])
    CompleteGroup.objects.create(user=user_data, question_group=q_group)
    return redirect('../../..')