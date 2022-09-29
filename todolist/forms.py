from django import forms
from todolist.models import Task

class TodoForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        label = {"title":"Title", "description":"Description"}