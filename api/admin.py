from django.contrib import admin
from api.models import Offer, Analytics

@admin.register(Offer)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'menulink', 'hilite')
    list_filter = ['product', 'description']
    search_fields = ['product', 'description']

@admin.register(Analytics)
class AnalyticsAdmin(admin.ModelAdmin):
    list_display = ('user', 'action')
    list_filter = ['user', 'action']
    search_fields = ['user', 'action']