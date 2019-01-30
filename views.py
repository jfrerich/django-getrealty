from django.shortcuts import render
# test
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import TemplateView
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.utils.html import format_html
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
    # return render(request, 'realty/getRealtyOptions.html',
    #               {'nbar': 'realty'})

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
        # value = '<a class="clickablename" href="#propertyDetailPage">{}</a>'.format(
        #     instance.r_num)
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

# @csrf_exempt
class ZeroConfigurationDatatableView(DatatableView):

    model = RealtyModel
    datatable_class = MyDatatable
    template_name = "realty/mymodel_list.html"
    # model.objects.all().filter(r_num='R38849')
    # print('RealtyModel.objects.all', RealtyModel.objects.all(), "\n")
    # print('get_queryset', RealtyModel.objects.get_queryset(), "\n")
    # print('get_context_data', RealtyModel.objects.get_context_data(), "\n")
    # structure_template = 'realty/bootstrap_structure.html'
    # structure_template = 'datatableview/bootstrap_structure.html'
    # print('jason', DatatableView.get_context_data)
    # AJAX response handler

    # print('RealtyModel.objects.all', RealtyModel.objects.get_datatable_kwargs(), "\n")

    # def get_queryset(self, *args, **kwargs):
    #     # these all work
    #     # print('ID', self.request.GET.get('ID'))
    #     print('r_num', self.request.GET.get('r_num'))
    #     return RealtyModel.objects.all().filter(r_num='R38849')
        # return RealtyModel.objects.all().filter(id='1')
        # return RealtyModel.objects.all().filter(
        #     Subd__startswith='LAKE BASTROP ESTATES')
        # return RealtyModel.objects.all().filter(r_num=self.request.GET.get('r_num'))
        # return RealtyModel.objects.all().filter(
        #     Property_Interest='Vetting')


class detailview(ZeroConfigurationDatatableView):
    template_name = "realty/propertydetail.html"
    manor_status = RealtyModel.objects.filter(r_num='R38849')

    # return render_to_response('realty/propertydetail.html', {'jason': 'jason'})
    # print(my_values)
    # print('get_context_data', RealtyModel.objects.all().filter(r_num='R38849').values(), "\n")
    # print(context)
    # print([field.name for field in RealtyModel._meta.fields])
    def compute_context(self, request, username):
        super(ZeroConfigurationDatatableView).as_view()(request)

    # print(response)
    # def get_context_data(self, **kwargs):
    #     return {'jason frerich': 'junk'}
    #
    # def get_fields(self):
    #     my_values =  RealtyModel.objects.all().filter(r_num='R38849').values()
    #     print('my_values', my_values)
    #     return my_values
        # return [(field.name, field.value_to_string(self)) for field in RealtyModel._meta.fields]

    # render_to


class ViewDbListJson(BaseDatatableView):

    # print("_querydict", BaseDatatableView._querydict)
    model = RealtyModel
    # print("RealtyModel", BaseDatatableView._querydict)
    columns = ['r_num',
               # 'rpg',
               'Property_Interest',
               'Files_xx_BillsF',
               'Files_xx_HistF',
               'Files_xx_DetF',
               'Files_xx_DataF',
               'Maps_xx_GIS',
               'Maps_xx_Map',
               'NOTES',
               'Subd',
               'Prop_Details_xx_Acres',
               'Prop_Details_xx_AssessVal',
               'Prop_Details_xx_AssessMinDue',
               'Tax_Due_xx_PctToAss',
               'Tax_Due_xx_TotAmtDue',
               'DatePulled',
               'TaxDates_xx_OldestDue',
               'TaxDates_xx_LastPaid',
               'TaxDates_xx_LastYrPaid',
               'Different_xx_Addr',
               'Different_xx_Zip',
               'Different_xx_State',
               'NHS_imp',
               'InstallYr',
               'TimesSold_xx_Num',
               'TimesSold_xx_Last',
               'Appraised_xx_AppPctOfMax',
               'Appraised_xx_AppLastVal',
               'Appraised_xx_AppMaxVal',
               'AppraisedMaxReduced_xx_AppMaxAmt',
               'AppraisedMaxReduced_xx_AppMaxYr',
               'Assess_xx_AssPctOfMax',
               'Assess_xx_AssLastVal',
               'Assess_xx_AssMaxVal',
               'AssessMaxReduced_xx_AssMaxAmt',
               'AssessMaxReduced_xx_AssMaxYr',
               'ImpNHS_xx_LastPctOfMax',
               'ImpNHS_xx_LastVal',
               'ImpNHS_xx_MaxVal',
               'ImpNHSMaxReduced_xx_MaxAmt',
               'ImpNHSMaxReduced_xx_MaxYr',
               'ImpHS_xx_ihsPctOfMax',
               'ImpHS_xx_ihsLastVal',
               'ImpHS_xx_ihsMaxVal',
               'ImpHSMaxReduced_xx_ihsMaxAmt',
               'ImpHSMaxReduced_xx_ihsMaxYr',
               'LandHS_xx_lhsPctOfMax',
               'LandHS_xx_lhsLastVal',
               'LandHS_xx_lhsMaxVal',
               'LandHSMaxReduced_xx_lhsMaxAmt',
               'LandHSMaxReduced_xx_lhsMaxYr',
               'LandNHS_xx_lnhsPctOfMax',
               'LandNHS_xx_lnhsLastVal',
               'LandNHS_xx_lnhsMaxVal',
               'LandNHSMaxReduced_xx_lnhsMaxAmt',
               'LandNHSMaxReduced_xx_lnhsMaxYr',
               'DaysLate_xx_Curr',
               'DaysLate_xx_Max',
               'PctDiffAddr',
               'PropAddr',
               'OwnerAddr',
               'OwnerName',
               'LegalDesc',
               ]

    def render_column(self, row, column):
        # render custom columns

        # r_num column
        if column == 'r_num':
            my_rnumber = '{0}'.format(row.r_num)
            link = format_html(
                # "<a class=\"clickablename\" href=\"Junk\">{}</a>",
                "<a class=\"clickablename\" href=\"#propertyDetailPage\">{}</a>",
                my_rnumber)
            return link

        # if column == 'Files_xx_BillsF':
        m = re.search(r"Files_xx_(\w+)F", column)
        if m:
            link_name = m.group(1)
            my_file = '{0}'.format(row.Files_xx_BillsF)
            link = format_html("<a class=\"clickablename\" href=\"{}\">{}</a>",
                               my_file, link_name)
            return link

        # Maps columns
        if column == 'Maps_xx_GIS':
            my_file = '{0}'.format(row.Maps_xx_GIS)
            link = format_html(
                "<a class=\"clickablename\" href=\"{}\">GIS</a>",
                my_file)
            return link

        # if column == 'user':
        #     # escape HTML for security reasons
            # return escape('{0} {1}'.format(row.customer_firstname,
            #                                row.customer_lastname))
        #     return 'link'
        else:
            return super(ViewDbListJson, self).render_column(row, column)
