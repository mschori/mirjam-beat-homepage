import django_tables2 as tables
from .models import Contribution
from helpers import string_helper
from django.utils.html import format_html
from django.utils.translation import gettext as _


class ContributionTable(tables.Table):
    class Meta:
        model = Contribution
        fields = ('product', 'comment', 'amount', 'is_self_buy')
        attrs = {'class': 'table table-hover', 'th': {'class': 'text-secondary link-unstyled'}}

    product = tables.Column(verbose_name=string_helper.translate_lazy_string(_('Product')))
    comment = tables.Column(verbose_name=string_helper.translate_lazy_string(_('Comment')))
    amount = tables.Column(verbose_name=string_helper.translate_lazy_string(_('Amount')))
    is_self_buy = tables.BooleanColumn(verbose_name=string_helper.translate_lazy_string(_('You buy it')),
                                       attrs={'td': {'class': 'text-center'}})
    actions = tables.TemplateColumn(verbose_name=string_helper.translate_lazy_string(_('Actions')), orderable=False,
                                    template_name='wishlist/objects/action-buttons-list-contributions.html')

    def render_comment(self, value, record):
        return format_html('<span data-bs-toggle="tooltip" title="{}">{}</span>', value,
                           string_helper.cust_string_end(value, 50, True))

    def render_amount(self, value, record):
        return f'CHF {value:.2f}'


class ContributionTableShort(tables.Table):
    class Meta:
        model = Contribution
        fields = ('product', 'amount', 'is_self_buy')
        attrs = {'class': 'table table-hover', 'th': {'class': 'text-secondary link-unstyled'}}

    product = tables.Column(verbose_name=string_helper.translate_lazy_string(_('Product')))
    amount = tables.Column(verbose_name=string_helper.translate_lazy_string(_('Amount')))
    is_self_buy = tables.BooleanColumn(verbose_name=string_helper.translate_lazy_string(_('Selfbuy')),
                                       attrs={'td': {'class': 'text-center'}})
    actions = tables.TemplateColumn(verbose_name=string_helper.translate_lazy_string(_('Actions')), orderable=False,
                                    template_name='wishlist/objects/action-buttons-list-contributions.html')

    def render_product(self, value, record):
        return format_html('<span data-bs-toggle="tooltip" title="{}">{}</span>', value,
                           string_helper.cust_string_end(value.title, 7, True))

    def render_amount(self, value, record):
        return f'CHF {value:.2f}'
