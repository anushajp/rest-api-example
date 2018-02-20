from rest_framework import serializers
from .models import Question, Answer


class AnswerSerializer(serializers.ModelSerializer):
    created_on = serializers.DateTimeField(format="%Y %B %d T%H:%M:%S", required=False,
                                             read_only=True)
    class Meta:
        model = Answer
        fields = '__all__'
        exclude = 'updated_on'


class QuestionSerializer(serializers.ModelSerializer):
    answer = AnswerSerializer(read_only=True, many=True)
    created_on = serializers.DateTimeField(format="%Y %B %d T%H:%M:%S", required=False,
                                             read_only=True)
    class Meta:
        model = Question
        fields = '__all__'
        exclude = 'updated_on'