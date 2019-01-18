from django.shortcuts import render
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from realty.models import TestModel


def home(request):
    return render(request, 'realty/index.html', {'nbar': 'realty'})


def viewDb(request):
    return render(request, 'realty/viewDb.html', {'nbar': 'realty'})


def overview(request):
    return render(request, 'realty/overview.html', {'nbar': 'realty'})


def query(request):
    return render(request, 'realty/getRealtyOptions.html', {'nbar': 'realty'})


def detail(request):
    return render(request, 'realty/propertydetail.html', {'nbar': 'realty'})


def testpage(request):
    return render(request, 'realty/test_page.html', {'nbar': 'realty'})


def testPage2(request):
    return render(request, 'realty/testPage2.html', {'nbar': 'realty'})


class ViewDbList(TemplateView):
    template_name = 'realty/viewDb.html'


class ViewDbListJson(BaseDatatableView):

    model = TestModel
    # columns and order columns are provided by datatables in the request using
    # "name" in columns definition
