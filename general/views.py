# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.http import JsonResponse, HttpResponse

# Create your views here.

def home(request):
	c = {}

	return render_to_response('general/home.html',c)



def calculate_significance(request):
	d = {}


	control_visitors = int( request.GET['control_visitors'] )
	variation_visitors = int( request.GET['variation_visitors'] )
	
	control_conversions = int( request.GET['control_conversions'] )
	variation_conversions = int( request.GET['variation_conversions'] )
	significance = ( ( control_visitors * variation_visitors) + (control_conversions * control_conversions) ) /10
	if significance > 0.9 :
		significance = 0.9

	d['significance'] = str(significance)

	return JsonResponse(d)
