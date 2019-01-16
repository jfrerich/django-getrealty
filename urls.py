from django.urls import path

from . import views
from .views import TestModelList, TestModelListJson
# from .views import TestModelList

urlpatterns = [
    path('', views.home, name='home'),
    path('overview.html', views.overview, name='overview'),
    path('viewDb.html', views.viewDb, name='viewDb'),
    path('propertydetail.html', views.propertydetail, name='propertydetail'),
    path('getRealtyOptions.html',
         views.getRealtyOptions,
         name='getrealtyOptions'),
    path('test_page.html', views.test_page, name='test_page'),
    path('testPage2.html', views.testPage2, name='testPage2'),
    path('navbartop.html', views.navbartop, name='navbartop'),
    path('testmodel_list.html', views.TestModelList.as_view(), name='testmodel'),
    path('testmodel_data', TestModelListJson.as_view(), name="testmodel_list_json"),
    # path('testmodel_list.html', TestModelList.as_view(), name='testmodel'),
]
