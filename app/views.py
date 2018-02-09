# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

# Create your views here.
@csrf_exempt
def home(request):
    print(request)
    return HttpResponse("hi")