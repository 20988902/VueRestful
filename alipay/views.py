from django.shortcuts import render,redirect
from alipay.utils.pay import AliPay



def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    goods = ''
    money = float(request.POST.get('price'))

    return redirect('')