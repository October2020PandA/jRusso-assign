from django.db import models
from logreg.models import User

# Create your models here.
class QuestionGroup(models.Model):
    group_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, related_name='question_groups', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuestionType(models.Model):
    type_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Question(models.Model):
    question = models.TextField(max_length=255)
    answer = models.TextField(max_length=255)
    question_type = models.ForeignKey(QuestionType, related_name='questions', on_delete=models.CASCADE)
    question_group = models.ForeignKey(QuestionGroup, related_name='questions', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class QuestionChoice(models.Model):
    question_choice = models.CharField(max_length=255)
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)