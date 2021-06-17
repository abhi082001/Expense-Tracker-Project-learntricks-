from django.shortcuts import render, HttpResponseRedirect
from .forms import Userentry
from .models import Uinput,exptable,tagtable
from django.contrib.auth.models import User, auth
from .filters import OrderFilter
from django.db.models import Sum
from .utils import get_plot, get_plot_pie
from django.contrib import messages

# Create your views here.
def user_input(request):
    if request.method == 'POST':
        if request.POST.get('exptype'):
            #savevalue1 = Uinput()
            savevalue1 = request.POST.get('exptype')
               
        
        if request.POST.get('tagname'):
            #savevalue2 = Uinput()
            savevalue2 = request.POST.get('tagname')
            
       
        fm = Userentry(request.POST)
        if fm.is_valid():
            m = fm.cleaned_data['Month']
            em = fm.cleaned_data['Day']
            #pw = fm.cleaned_data['Expinc']
            #dw = fm.cleaned_data['Tag']
            fw = fm.cleaned_data['Amount']
            reg = Uinput(Month=m, Day=em,Expinc=savevalue1,Tag=savevalue2,Amount=fw,user=request.user)
            reg.save()
            fm = Userentry()
    else:
        fm = Userentry()
    exps = exptable.objects.all()
    tags = tagtable.objects.all()
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    stud = Uinput.objects.filter(user=log_user)
    myFilter = OrderFilter(request.GET, queryset=stud)
    
    stud = myFilter.qs
    return render(request,'entry.html',{'form':fm,'stu':stud,'myFilter': myFilter,'exps':exps,'tags':tags})

def analytics(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    stud = Uinput.objects.filter(user=log_user)
    myFilter = OrderFilter(request.GET, queryset=stud)
    stud = myFilter.qs
    stud_1 = stud.filter(Expinc = 'Income')
    sum_income = stud_1.aggregate(p1 = Sum('Amount'))
    stud_2 = stud.filter(Expinc = 'Expense')
    sum_expense = stud_2.aggregate(p2 = Sum('Amount'))
    if sum_income['p1'] == None:
        sum_income['p1'] =0
    if sum_expense['p2'] == None:
        sum_expense['p2'] =0
    sum_diff = int(sum_income['p1']) - int(sum_expense['p2'])
    X = [int(x.Day) for x in stud_2]
    Y = [int(y.Amount) for y in stud_2]
    x1 = [x1.Tag for x1 in stud_2]
    y1 = [int(y.Amount) for y in stud_2]
    P = [int(x.Day) for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [x1.Tag for x1 in stud_1]
    q1 = [int(y.Amount) for y in stud_1]

    d ={}
    for x in X:
        d[x]=0
    i=0
    for x in X:
        d[x] = d[x]+Y[i]
        i+=1
    X = list(d.keys())
    
    Y = list(d.values())

    d ={}
    for x in x1:
        d[x]=0
    i=0
    for x in x1:
        d[x] = d[x]+y1[i]
        i+=1
    x1 = list(d.keys())
    
    y1 = list(d.values())

    d ={}
    for x in P:
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d ={}
    for x in p1:
        d[x]=0
    i=0
    for x in p1:
        d[x] = d[x]+q1[i]
        i+=1
    p1 = list(d.keys())
    
    q1 = list(d.values())
    
    chart1 = get_plot(X,Y)
    chart2 = get_plot_pie(x1,y1)
    chart3 = get_plot(P,Q)
    chart4 = get_plot_pie(p1,q1)

    if request.GET.get('Month')!= None:
        if request.POST.get('bar'):
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart1})
        elif request.POST.get('pie'):
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart2})
        elif request.POST.get('bar1'):
            return render(request,'Analytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart3})
        elif request.POST.get('pie1'):
            return render(request,'Analytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart4})
        else:
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','s':"** select either of these two buttons **",'chart':False})
    
    else:
        if request.POST.get('bar'):
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart1})
        elif request.POST.get('pie'):
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart2})
        elif request.POST.get('bar1'):
            return render(request,'Analytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart3})
        elif request.POST.get('pie1'):
            return render(request,'Analytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart4})
        else:
            return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','s':"** select either of these two buttons **",'chart':False})

def ianalytics(request):
    if request.user.is_authenticated:
        log_user = request.user
    else:
        return HttpResponseRedirect('accounts/login')
    stud = Uinput.objects.filter(user=log_user)
    myFilter = OrderFilter(request.GET, queryset=stud)
    stud = myFilter.qs
    stud_1 = stud.filter(Expinc = 'Income')
    sum_income = stud_1.aggregate(p1 = Sum('Amount'))
    stud_2 = stud.filter(Expinc = 'Expense')
    sum_expense = stud_2.aggregate(p2 = Sum('Amount'))
    if sum_income['p1'] == None:
        sum_income['p1'] =0
    if sum_expense['p2'] == None:
        sum_expense['p2'] =0
    sum_diff = int(sum_income['p1']) - int(sum_expense['p2'])
    X = [int(x.Day) for x in stud_2]
    Y = [int(y.Amount) for y in stud_2]
    x1 = [x1.Tag for x1 in stud_2]
    y1 = [int(y.Amount) for y in stud_2]
    P = [int(x.Day) for x in stud_1]
    Q = [int(y.Amount) for y in stud_1]
    p1 = [x1.Tag for x1 in stud_1]
    q1 = [int(y.Amount) for y in stud_1]


    d ={}
    for x in P:
        d[x]=0
    i=0
    for x in P:
        d[x] = d[x]+Q[i]
        i+=1
    P = list(d.keys())
    
    Q = list(d.values())

    d ={}
    for x in p1:
        d[x]=0
    i=0
    for x in p1:
        d[x] = d[x]+q1[i]
        i+=1
    p1 = list(d.keys())
    
    q1 = list(d.values())
    
    chart3 = get_plot(P,Q)
    chart4 = get_plot_pie(p1,q1)

    if request.GET.get('Month')!= None:
        
        if request.POST.get('bar1'):
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart3})
        elif request.POST.get('pie1'):
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart4})
        else:
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','s':"** select either of these two buttons **",'chart':False})
    
    else:
        
        if request.POST.get('bar1'):
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart3})
        elif request.POST.get('pie1'):
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','chart':chart4})
        else:
            return render(request,'Ianalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':'All months','s':"** select either of these two buttons **",'chart':False})


def update_data(request,id):
    if request.method == 'POST':
        pi  = Uinput.objects.get(pk = id)
        fm = Userentry(request.POST, instance = pi)
        if fm.is_valid():
            fm.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = Uinput.objects.get(pk = id)
        fm = Userentry(instance = pi)
    return render(request,'update.html', {'form':fm})

def delete_data(request, id):
    if request.method == 'POST':
        
        pi = Uinput.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/userinput/user_input')
        