from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    question = models.CharField(max_length=300)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


class Answer(models.Model):
    answer = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)