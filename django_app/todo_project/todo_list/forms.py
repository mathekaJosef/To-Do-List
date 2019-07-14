from django import forms
from .models import List

class ListForm(forms.Form):
    class Meta:
        model = List
        fields = ['item', 'completed']