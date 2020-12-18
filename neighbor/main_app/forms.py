from django import forms
from .models import JobPost

class SearchingForm(forms.ModelForm):
  class Meta:
    model = JobPost
    fields = ['name']