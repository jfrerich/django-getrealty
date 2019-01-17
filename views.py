from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from realty.models import TestModel

# Create your views here.

class TestModelList(TemplateView):
    template_name = 'realty/testmodel_list.html'
    # template_name = 'realty/viewDb.html'

class TestModelListJson(BaseDatatableView):

    model = TestModel
    # columns and order columns are provided by datatables in the request using "name" in columns definition

