# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def site(request):
    return render(request, 'app1/index.html', {})
