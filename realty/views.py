from django.shortcuts import render
import re
from datatableview.views import DatatableView, Datatable

from realty.models import RealtyModel
from realty.forms import QueryForm


def home(request):
    return render(request, 'realty/index.html', {'nbar': 'realty'})


def viewDb(request):
    return render(request, 'realty/viewDb.html', {'nbar': 'realty'})


def viewModelDb(request):
    return render(request, 'realty/viewModelDb.html', {'nbar': 'realty'})


def overview(request):
    return render(request, 'realty/overview.html', {'nbar': 'realty'})


def query(request):
    return render(request,
                  'realty/getRealtyOptions.html',
                  {'nbar': 'realty',
                   'form': QueryForm()})


def detail(request):
    return render(request, 'realty/propertydetail.html', {'nbar': 'realty'})


def testpage(request):
    return render(request, 'realty/test_page.html', {'nbar': 'realty'})


def testPage2(request):
    return render(request, 'realty/testPage2.html', {'nbar': 'realty'})


class MyDatatable(Datatable):

    class Meta:
        request_method = 'POST'
        processors = {
            'r_num': 'get_rnum_link',
            'Files_xx_BillsF': 'get_file_link',
            'Files_xx_HistF': 'get_file_link',
            'Files_xx_DetF': 'get_file_link',
            'Files_xx_DataF': 'get_file_link',
            'Maps_xx_Map': 'get_map_link',
            'Maps_xx_GIS': 'get_external_maps_link',
        }

        def get_labels():
            '''rename all fields with _xx_ to shorten headers in table
            '''
            my_dict2 = dict()
            for field in RealtyModel._meta.get_fields():
                if re.search(r'_xx_', field.name):
                    result = re.sub(r'.*_xx_', '',   field.name)
                    my_dict2[field.name] = result
            return my_dict2

        labels = get_labels()

        structure_template = "realty/bootstrap_structure.html",

    def get_rnum_link(self, instance, **kwargs):
        value = '<a class="clickablename" href="#junkpage">{}</a>'.format(
            instance.r_num)
        return value

    def get_file_link(self, instance, **kwargs):
        '''create clickable link to local files
        '''
        field_name = kwargs.get('field_name')
        file_name = kwargs.get('default_value')
        short_name = re.sub('Files_xx_', '', field_name)
        short_name = re.sub('F$', '', short_name)

        value = '<a class="clickablename" href="{}">{}</a>'.format(
            file_name, short_name)
        return value

    def get_external_maps_link(self, instance, **kwargs):
        value = '<a class="clickablename" href="{}">GIS</a>'.format(
            instance.Maps_xx_GIS)
        return value

    def get_map_link(self, instance, **kwargs):
        value = ""
        if instance.Maps_xx_Map:
            value = '<a class="clickablename" href="{}">Map</a>'.format(
                instance.Maps_xx_GIS)
        return value


class ZeroConfigurationDatatableView(DatatableView):

    model = RealtyModel
    datatable_class = MyDatatable
    template_name = "realty/mymodel_list.html"


class detailview(ZeroConfigurationDatatableView):
    template_name = "realty/propertydetail.html"
    manor_status = RealtyModel.objects.filter(r_num='R38849')

    def compute_context(self, request, username):
        super(ZeroConfigurationDatatableView).as_view()(request)
