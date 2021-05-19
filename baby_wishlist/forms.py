from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
from helpers import babywishlist_helper


class ContributeForm(forms.Form):
    """
    Form for creating contributions.
    """
    contribute = forms.FloatField(required=True)
    comment = forms.CharField(required=True, widget=forms.Textarea)
    is_selfbuy = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        self.product = kwargs.pop('product')
        super().__init__(*args, **kwargs)

    def clean_is_selfbuy(self):
        if self.cleaned_data['is_selfbuy']:
            if not babywishlist_helper.is_progress_price_null(self.product):
                raise ValidationError(
                    _('Ups. Somebody already contributed to this product. Selfbuy is not possible.'),
                    code='invalid'
                )
            if not self.cleaned_data['contribute'] >= self.product.price_full:
                raise ValidationError(
                    _('You need to contribute the full price in order to buy this product on your selfe.')
                )
        return self.cleaned_data['is_selfbuy']
