from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from . import views
from .views import ZeroConfigurationDatatableView, detailview

urlpatterns = [
    path('', views.home, name='realty'),
    path('viewDb/', views.viewDb, name='viewDb'),
    path('viewModelDb_data/',
         csrf_exempt(ZeroConfigurationDatatableView.as_view()),
         name="viewModelDb_data"),
    path('overview/', views.overview, name='overview'),
    path('query/', views.query, name='query'),
    # path('detail/', views.detail, name='detail'),
    # path('detail/',
    #      detailview.as_view(template_name='realty/propertydetail.html'),
    #      name='detail'),
    path('detail/', detailview.as_view(), name='detail'),
    path('testpage/', views.testpage, name='testpage'),
    path('testPage2/', views.testPage2, name='testPage2'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
