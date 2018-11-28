from django.urls import path

from . import views

urlpatterns = [
    path('get_product/<slug:product>', views.get_product, name='get_product'),
    path('filter_products/<int:minprice>/<int:maxprice>', views.filter_products, name='filter_products'),
    path('get_all_offers', views.get_all_offers, name='get_all_offers'),
    path('save_offers', views.save_offers, name='save_offers'),
]