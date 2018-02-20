from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_by', 'created_on',)


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer', 'created_by', 'created_on',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
