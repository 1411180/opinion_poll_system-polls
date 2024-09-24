from django import forms
from .models import Poll, Question, Choice

class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['title', 'description']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['text']