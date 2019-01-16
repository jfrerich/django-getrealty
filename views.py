from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView

from realty.models import TestModel

# class TestModelList(request):
    # template_name = 'testmodel_list.html'

# def TestModelList(request):
#     return render(request, 'realty/testmodel_list.html')
class TestModelList(TemplateView):
    # template_name = 'realty/testmodel_list.html'
    template_name = 'realty/viewDb.html'

class TestModelListJson(BaseDatatableView):
    model = TestModel
    # columns and order columns are provided by datatables in the request using "name" in columns definition


def home(request):
    # return render(request, 'realty/node_modules/greatlyapp/index.html')
    # template = loader.get_template('realty/node_modules/greatlyapp/index.html')
    # print(template.render)
    # return HttpResponse(template.render())
    return render(request, 'realty/index.html')


def overview(request):
    return render(request, 'realty/overview.html')


def viewDb(request):
    return render(request, 'realty/viewDb.html')


def propertydetail(request):
    return render(request,
                  'realty/propertydetail.html')


def getRealtyOptions(request):
    return render(request,
                  'realty/getRealtyOptions.html')


def test_page(request):
    return render(request, 'realty/test_page.html')


def testPage2(request):
    return render(request, 'realty/testPage2.html')


def navbartop(request):
    return render(request, 'realty/navbartop.html')
