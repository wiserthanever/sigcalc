# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response

# Create your views here.

def home(request):
	c = {}

	return render_to_response('general/home.html',c)


