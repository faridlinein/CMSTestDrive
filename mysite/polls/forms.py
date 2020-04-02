from django import forms

from .models import Question


class PollWizardForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = []

