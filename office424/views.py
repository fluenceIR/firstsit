from django.shortcuts import render
from django.http import HttpResponse
from office424.models import *
# Create your views here.


def index(request):
    # return HttpResponse('hello world')
    # context = {'title': '424首页', 'list': range(10)}
    return render(request, 'office424/index.html')


def person_info(request):
    personlist = PersonInfo.objects.all()
    context = {'person_list': personlist}
    return render(request, 'office424/personInfo.html', context)


def trade_info(request):
    tradelist = TradeInfo.objects.all()
    context = {'tradelist': tradelist}
    return render(request, 'office424/tradeInfo.html', context)

