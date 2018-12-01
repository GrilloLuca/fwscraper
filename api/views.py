from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.template.loader import render_to_string
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt

import json
import urllib.request
import certifi
from api.models import Offer, Analytics
from bs4 import BeautifulSoup
import re
import os
import getpass
import django

url = "https://www.fastweb.it/"

"""
Scraping and saving data from db
returns True if success
api/save_offers
"""
def save_offers(request):

    request = urllib.request.Request(url)
    response = urllib.request.urlopen(url, cafile=certifi.where())

    soup = BeautifulSoup(response, 'html.parser')

    # OFFERS FW + SKY
    col_offers_fw = soup.findAll("div", { "class" : "column offerte_fw" })
    col_offers_sky = soup.findAll("div", { "class" : "column offerte_sky" })
    
    offers = col_offers_fw + col_offers_sky
    for offer in offers:
        product = offer.find("span", { "class" : "product" })
        menulink = offer.find("a", { "class" : "menulink" })
        description = offer.find("span", { "class" : "description" })

        prices = offer.findAll("span", { "class" : "hilite" })
        for price in prices:
            number = price.find("span", { "class" : "number" })
        
        default = {
            'menulink': menulink['href'],
            'hilite': float(number.text.replace('€', '').replace(',', '.')),
            'description': description.text
        }
        offer, created = Offer.objects.update_or_create(
            product = product.text,
            defaults = default
        )
        # update if exixts
        if not created:
            offer.menulink = default['menulink']
            offer.hilite = default['hilite']
            offer.description = default['description']

         
    return JsonResponse({"result": True})

"""
Get all products without filter and order
api/get_all_offers/minprice/maxprice
"""
def get_all_offers(request):

    offers = Offer.objects.all()
    return JsonResponse(toJson(offers))

"""
Filtering product by min price and max price
api/filter_products/minprice/maxprice
"""
def filter_products(request, minprice, maxprice):

    offers = Offer.objects.filter(hilite__range=(minprice, maxprice))
    return JsonResponse(toJson(offers))

"""
Filtering product by min price and max price and sort by fieldname
api/filter_products/minprice/maxprice/sort/order
"""
def filter_and_sort_products(request, minprice, maxprice, sort, order):

    _sort = sort
    if order == 'desc':
        _sort = '-%s' % sort

    offers = Offer.objects.filter(hilite__range=(minprice, maxprice)).order_by(_sort)
    return JsonResponse(toJson(offers))

"""
convert Django model to json object
"""
def toJson(offers):

    obj = {
        'url': url,
        'offers': []
    }

    for offer in offers:
        obj['offers'].append({
            'product': offer.product,
            'menulink': offer.menulink,
            'hilite': offer.hilite,
            'description': offer.description
        })

    return obj

@csrf_exempt
def log_analytics(request):
    if request.method == 'POST':
        response = json.loads(request.body)
        print(response['action'], response['data'])

        user = getpass.getuser()
        Analytics.objects.create(user=user, action=response['action'], data=response['data'])

    return JsonResponse({'response': request.user.username})


@ensure_csrf_cookie
def token_security(request):
    return JsonResponse({'token': django.middleware.csrf.get_token(request)}) 
