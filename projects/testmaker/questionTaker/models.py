from django.db import models
from questionCreator.models import QuestionGroup, Question
from logreg.models import User

# Create your models here.
class Answer(models.Model):
    user = models.ForeignKey(User, related_name='answers', on_delete=models.CASCADE)
    question_group = models.ForeignKey(QuestionGroup, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CompleteGroup(models.Model):
    user = models.ForeignKey(User, related_name='complete_groups', on_delete=models.CASCADE)
    question_group = models.ForeignKey(QuestionGroup, related_name='complete_groups', on_delete=models.CASCADE)
    is_completed = models.BooleanField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)