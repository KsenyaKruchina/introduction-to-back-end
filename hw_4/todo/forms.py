from django import forms
from .models import Thing


class CreateThingForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True,
                            widget=forms.TextInput(attrs={'class': 'form-control',
                                                          'placeholder': 'Enter Todo title',}))
    description = forms.CharField(min_length=0, max_length=3000, required=False,
                                  widget=forms.TextInput(attrs={'class': 'form-control',
                                                                'placeholder': 'Enter Todo description', }))
    due_date = forms.DateField(required=True, widget=forms.DateInput(attrs={'type': 'date'}))
    status = forms.BooleanField(required=False)

