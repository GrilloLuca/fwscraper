from django.urls import path

from . import views

urlpatterns = [
    path('save_offers', views.save_offers, name='save_offers'),
    path('get_all_offers', views.get_all_offers, name='get_all_offers'),
    path('log_analytics', views.log_analytics, name='log_analytics'),
    path('token_security', views.token_security, name='token_security'),
    
    path('filter_products/<int:minprice>/<int:maxprice>', 
        views.filter_products, 
        name='filter_products'),

    path('filter_and_sort_products/<int:minprice>/<int:maxprice>/<slug:sort>/<slug:order>', 
        views.filter_and_sort_products, 
        name='filter_and_sort_products'),
]