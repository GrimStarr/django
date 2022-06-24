from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from trade.trade import *
# Create your views here.

def buy(request, type,stoploss,repeat = 1):
    stop = float(stoploss) * 0.01
    goldbuy(type,stop,repeat)
    return HttpResponse("success")