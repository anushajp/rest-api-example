from django.shortcuts import render
from .models import Question
from .serializers import QuestionSerializer
from rest_framework import viewsets
from rest_framework.response import Response


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer = QuestionSerializer(queryset, many=True)
    def list(self, request):
        # queryset = Question.objects.all()
        return Response(self.serializer.data)

