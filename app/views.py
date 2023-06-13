from django.shortcuts import render

# Create your views here.

def wish(request):
    d={'name':'Ram','age':22}
    return render(request,'wish.html',context=d)

def condition_1(request):
    d={'a':25}
    return render(request,'condition_1.html',context=d)

def condition_2(request):
    d={'a':20,'b':30}
    return render(request,'condition_2.html',context=d)

def condition_3(request):
    d={'a':20,'b':30,'c':40}
    return render(request,'condition_3.html',context=d)

def condition_4(request):
    d={'a':20,'b':300,'c':40}
    return render(request,'condition_4.html',context=d)

def loop(request):
    d={'name':''}
    return render(request,'loop.html',context=d)



