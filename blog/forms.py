from django import forms


class InputForm(forms.Form):
    years = forms.CharField(label='years', max_length=4)
    months = forms.CharField(label='months', max_length=2)
    curr = forms.CharField(label='curr', max_length=8)