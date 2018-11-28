from django.shortcuts import render
from django.http import JsonResponse
from django.template.loader import render_to_string

import json
import urllib.request
import certifi
from api.models import Offer
from bs4 import BeautifulSoup
import re

url = "https://www.fastweb.it/"

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

def get_all_offers(request):

    offers = Offer.objects.all()

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

    return JsonResponse(obj)

def get_product(request, product):

    offers = Offer.objects.filter(product__contains=product)

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

    return JsonResponse(obj)


def filter_products(request, minprice, maxprice):

    offers = Offer.objects.filter(hilite__range=(minprice, maxprice))

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

    return JsonResponse(obj)
