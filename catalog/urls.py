from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('product/<int:pk>/', product, name='product'),
]
