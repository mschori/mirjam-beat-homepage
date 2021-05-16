from django import forms


class ContributeForm(forms.Form):
    contribute = forms.FloatField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
