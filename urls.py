from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views
from .views import TestModelList, TestModelListJson

urlpatterns = [
    path('', views.home, name='realty'),
    path('viewDb/', views.viewDb, name='viewDb'),
    # path('viewDb/', views.TestModelList.as_view(), name='viewDb'),
    path('overview/', views.overview, name='overview'),
    path('query/', views.query, name='query'),
    path('detail/', views.detail, name='detail'),
    path('testpage/', views.testpage, name='testpage'),
    path('testPage2/', views.testPage2, name='testPage2'),
    path('testmodel/', TestModelList.as_view(), name='testmodel'),
    path('testmodel_data/', TestModelListJson.as_view(),
         name="testmodel_list_json"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
