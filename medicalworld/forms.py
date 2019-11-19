from django import forms

class MedForm(forms.Form):
    med_name = forms.CharField(label='Equipment Type', max_length=100)
    amount = forms.IntegerField()