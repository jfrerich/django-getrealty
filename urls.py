from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# from . import views
from .views import TestModelList, TestModelListJson

urlpatterns = [
    path('testmodel/', TestModelList.as_view(), name='testmodel'),
    path('testmodel_data/', TestModelListJson.as_view(),
         name="testmodel_list_json"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
