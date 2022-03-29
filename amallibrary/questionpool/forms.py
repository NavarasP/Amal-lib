import json
from django import forms
from .models import *
from django.forms import NumberInput, TextInput,Select

class Qform(forms.ModelForm):
    question_subject = forms.ModelChoiceField(queryset=subject.objects.all(),empty_label="Subject",widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Subject',}))
    question_department = forms.ModelChoiceField(queryset=department.objects.all(),empty_label="Department",widget=Select(attrs={'class':'bg-gray-200 appearance-none border-2 border-gray-200 rounded-full w-7/12 py-2 px-4 text-center text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-purple-500','placeholder':'Enter Department'}))
    class Meta:
        model = question
        fields = ['question_ques','question_answer','question_subject','question_department']

