from django import forms
from .models import summary


class summaryForm(forms.ModelForm):
    class Meta():
        model = summary
        fields = '__all__'
