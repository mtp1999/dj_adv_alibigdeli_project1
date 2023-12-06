from django import forms
from appTodo.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["user", "name", "status"]
