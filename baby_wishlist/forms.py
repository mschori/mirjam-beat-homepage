from django import forms


class ContributeForm(forms.Form):
    """
    Form for creating contributions.
    """
    contribute = forms.FloatField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
