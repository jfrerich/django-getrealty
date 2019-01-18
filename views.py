from django.shortcuts import render
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from realty.models import TestModel


def home(request):
    return render(request, 'realty/index.html')
    # template_name = 'realty/viewDb.html'


def viewDb(request):
    print("In Here!")
    return render(request, 'viewDb.html')
    # template_name = 'realty/viewDb.html'


def overview(request):
    return render(request, 'realty/overview.html')


class TestModelList(TemplateView):
    template_name = 'realty/testmodel_list.html'
    # template_name = 'realty/viewDb.html'


class TestModelListJson(BaseDatatableView):

    model = TestModel
    # columns and order columns are provided by datatables in the request using
    # "name" in columns definition
