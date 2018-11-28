from django.contrib import admin
from api.models import Offer

@admin.register(Offer)
class OffersAdmin(admin.ModelAdmin):
    list_display = ('product', 'description', 'menulink', 'hilite')
    list_filter = ['product', 'description']
    search_fields = ['product', 'description']