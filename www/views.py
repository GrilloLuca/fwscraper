from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json

from django.conf import settings

import requests

def index(request):

    print(request.POST)

    url = 'http://%s/api/save_offers' % request.get_host()
    r = requests.get(url, params=request.GET)
    
    template = loader.get_template('www/index.html')
    context = {
        'response': json.loads(r.content)
    }
    return HttpResponse(template.render(context, request))