from django import forms


class CreateThingForm(forms.Form):
    title = forms.CharField(min_length=1, max_length=255, required=True)
    description = forms.CharField(min_length=0, max_length=3000, required=False)
    due_date = forms.DateField(required=True)
    status = forms.BooleanField(required=False)
