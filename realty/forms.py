from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Column, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class QueryForm(forms.Form):
    rnumbers = forms.CharField(label='Rnumbers', max_length=100)
    subdivisions = forms.CharField(label='Subdivisions', max_length=100)
    counties = forms.CharField(label='Counties', max_length=100)
    min_acres = forms.CharField(label='Min Acres', max_length=100)
    max_acres = forms.CharField(label='Max Acres', max_length=100)
    min_value = forms.CharField(label='Min Value', max_length=100)
    max_value = forms.CharField(label='Max Value', max_length=100)

    sql_search = forms.CharField(label='SQL Search', max_length=100)
    sql_where = forms.CharField(label='SQL Search', max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-4'
        self.helper.field_class = 'col-lg-8'
        self.helper.layout = Layout(
                'rnumbers',
                'subdivisions',
                'counties',
                'min_acres',
                'max_acres',
                'min_value',
                'max_value',
                HTML('<hr/>'),
                'sql_search',
                'sql_where',
        )
