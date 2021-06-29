from django.shortcuts import render, HttpResponseRedirect
from .forms import Userentry
from .forms1 import Userentry_1
from .models import Uinput,exptable,tagtable,tagtable_income
from django.contrib.auth.models import User, auth
from .filters import OrderFilter, OrderFilter1
from django.db.models import Sum
from .utils import get_plot, get_plot_pie
from django.contrib import messages
from datetime import date
import datetime

# Create your views here.
def user_input(request):
    today = date.today()
    m=today.month
    d = today.day
    datetime.datetime.now()
    if m==1:
        mon = "January"
    elif m==2:
        mon = "February"
    elif m==3:
        mon = "March"
    elif m==4:
        mon = "April"
    elif m==5:
        mon = "May"
    elif m==6:
        mon = "June"
    elif m==7:
        mon = "July"
    elif m==8:
        mon = "August"
    elif m==9:
        mon = "September"
    elif m==10:
        mon = "October"
    elif m==11:
        mon = "November"
    elif m==12:
        mon = "December"
    if request.method == 'POST':
        
            
        savevalue1 = None 
        
        if request.POST.get('tagname1'):
            
            savevalue1 = request.POST.get('tagname1')

        savevalue2 = None        
        if request.POST.get('month'):
            
            savevalue2 = request.POST.get('month')

        savevalue3 = None        
        if request.POST.get('day'):
            
            savevalue3 = request.POST.get('day')

        fm = Userentry(request.POST)
        if fm.is_valid():
            #m = fm.cleaned_data['Month']
            #em = fm.cleaned_data['Day']
            #pw = fm.cleaned_data['Expinc']
            #dw = fm.cleaned_data['Tag']
            fw = fm.cleaned_data['Amount']
            if savevalue1!=None and savevalue2!=None and savevalue3!=None:
                messages.info(request, 'Added successfully')
                reg = Uinput(Month=savevalue2, Day=savevalue3,Expinc='Expense',Tag=savevalue1,Amount=fw,user=request.user)
            else:
                messages.info(request, 'Please enter all values')
                return HttpResponseRedirect('user_input')
            reg.save()
            fm = Userentry()
            if request.user.is_authenticated:
                log_user = request.user
            else:
                return HttpResponseRedirect('accounts/login')
            stud = Uinput.objects.filter(user=log_user)
            stud1 = stud.filter(Month = mon)
    else:
        fm = Userentry()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
        stud = Uinput.objects.filter(user=log_user)            
        stud1 = stud.filter(Month = mon)

    savevalue = mon        
    if request.GET.get('month'):
        savevalue = request.GET.get('month')
        
        if savevalue != "All months" and savevalue != "p":
            stud1 = stud.filter(Month=savevalue)
        elif savevalue == "All months":
            stud1 = stud
        elif savevalue=='p':
            stud1 = stud.filter(Month=mon)
    myFilter = OrderFilter1(request.GET, queryset=stud1)
    stud1 = myFilter.qs
    
    
    stud1 = stud1.order_by('Month','-Day')
    exps = exptable.objects.all()
   
    tags = tagtable.objects.all()
            
    
    if savevalue!='p':
        return render(request,'starter_expense.html',{'form':fm,'stu':stud1,'myFilter': myFilter,'tags':tags,'f':int(m),'d':int(d),'a':savevalue+' Expense and income','save':savevalue})
    elif savevalue=='p':
        return render(request,'starter_expense.html',{'form':fm,'stu':stud1,'myFilter': myFilter,'tags':tags,'f':int(m),'d':int(d),'a':mon + ' Expense and income','save':savevalue})
    
def user_input1(request):
    today = date.today()
    m=today.month
    d = today.day
    datetime.datetime.now()
    if m==1:
        mon = "January"
    elif m==2:
        mon = "February"
    elif m==3:
        mon = "March"
    elif m==4:
        mon = "April"
    elif m==5:
        mon = "May"
    elif m==6:
        mon = "June"
    elif m==7:
        mon = "July"
    elif m==8:
        mon = "August"
    elif m==9:
        mon = "September"
    elif m==10:
        mon = "October"
    elif m==11:
        mon = "November"
    elif m==12:
        mon = "December"
    if request.method == 'POST':
        
               
        savevalue2 = None
        if request.POST.get('tagname2'):
            
            savevalue2 = request.POST.get('tagname2')
            
        savevalue3 = None        
        if request.POST.get('month'):
            
            savevalue3 = request.POST.get('month')

        savevalue4 = None        
        if request.POST.get('day'):
            
            savevalue4 = request.POST.get('day')
        fm = Userentry(request.POST)
        if fm.is_valid():
            #m = fm.cleaned_data['Month']
            #em = fm.cleaned_data['Day']
            fw = fm.cleaned_data['Amount']
            if savevalue2!=None and savevalue3!=None and savevalue4!=None:
                messages.info(request, 'Added successfully')
                reg = Uinput(Month=savevalue3, Day=savevalue4,Expinc='Income',Tag=savevalue2,Amount=fw,user=request.user)
            else:
                messages.info(request, 'Please enter all values')
                return HttpResponseRedirect('user_input1')
            reg.save()
            fm = Userentry()
            if request.user.is_authenticated:
                log_user = request.user
            else:
                return HttpResponseRedirect('accounts/login')
            stud = Uinput.objects.filter(user=log_user)
            stud1 = stud.filter(Month = mon)
    else:
        fm = Userentry()
        if request.user.is_authenticated:
                log_user = request.user
        else:
            return HttpResponseRedirect('accounts/login')
        stud = Uinput.objects.filter(user=log_user)
        stud1 = stud.filter(Month = mon)

    savevalue = mon        
    if request.GET.get('month'):
        savevalue = request.GET.get('month')
        if savevalue != "All months" and savevalue != "p":
            stud1 = stud.filter(Month=savevalue)
        elif savevalue == "All months":
            stud1 = stud
        elif savevalue=='p':
            stud1 = stud.filter(Month=mon)
    myFilter = OrderFilter1(request.GET, queryset=stud1)
    stud1 = myFilter.qs
    
    stud1 = stud1.order_by('Month','-Day')
    exps = exptable.objects.all()
   
    tags = tagtable_income.objects.all()

    if savevalue!='p':
        return render(request,'starter_income.html',{'form':fm,'stu':stud1,'myFilter': myFilter,'tags':tags,'f':int(m),'d':int(d),'a':savevalue+' Expense and income','save':savevalue})
    elif savevalue=='p':
        return render(request,'starter_income.html',{'form':fm,'stu':stud1,'myFilter': myFilter,'tags':tags,'f':int(m),'d':int(d),'a':mon+ ' Expense and income','save':savevalue})

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

    if request.GET.get('Month')!= None and request.GET.get('Month')!= '':
        if request.POST.get('bar'):
            return render(request,'starter_expanalytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart1,'d':'No record of expense in this month'})
        elif request.POST.get('pie'):
            return render(request,'starter_expanalytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart2,'d':'No record of expense in this month'})
        
        else:
            return render(request,'starter_expanalytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','s':"** select either of these two buttons **",'chart':False,'d':'No record of expense in this month'})
    
    else:
        return render(request,'starter_expanalytics.html',{'myFilter': myFilter,'d':"Add a month in month filter to see that month's amounts and graphs",'sum_income':'-','sum_expense':'-','sum_diff':'-'})

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

    if request.GET.get('Month')!= None and request.GET.get('Month')!= '':
        
        if request.POST.get('bar1'):
            return render(request,'starter_incanalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart3,'d':'No record of income in this month'})
        elif request.POST.get('pie1'):
            return render(request,'starter_incanalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','chart':chart4,'d':'No record of income in this month'})
        else:
            return render(request,'starter_incanalytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'m':request.GET.get('Month') + ' month','s':"** select either of these two buttons **",'chart':False,'d':'No record of income in this month'})
    
    else:
        return render(request,'starter_incanalytics.html',{'myFilter': myFilter,'d':"Add a month in month filter to see that month's amounts and graphs",'sum_income':'-','sum_expense':'-','sum_diff':'-'})
        


def update_data(request,id):
    if request.method == 'POST':
        pi  = Uinput.objects.get(pk = id)
        fm1 = Userentry_1(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = Uinput.objects.get(pk = id)
        fm1 = Userentry_1(instance = pi)
    return render(request,'update.html', {'form':fm1})

def update_data1(request,id):
    if request.method == 'POST':
        pi  = Uinput.objects.get(pk = id)
        fm1 = Userentry_1(request.POST, instance = pi)
        if fm1.is_valid():
            fm1.save()
            messages.info(request, 'Updated successfully')
    else:
        pi  = Uinput.objects.get(pk = id)
        fm1 = Userentry_1(instance = pi)
    return render(request,'update1.html', {'form':fm1})

def delete_data(request, id):
    if request.method == 'POST':
        
        pi = Uinput.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/userinput/user_input')

def delete_data1(request, id):
    if request.method == 'POST':
        
        pi = Uinput.objects.get(pk = id)
        pi.delete()
        return HttpResponseRedirect('/userinput/user_input1')
        