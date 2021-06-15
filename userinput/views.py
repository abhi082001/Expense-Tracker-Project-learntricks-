from django.shortcuts import render
from .forms import Userentry
from .models import Uinput
from django.contrib.auth.models import User, auth
from .filters import OrderFilter
from django.db.models import Sum
from .utils import get_plot, get_plot_pie

# Create your views here.
def user_input(request):
    if request.method == 'POST':
        fm = Userentry(request.POST)
        if fm.is_valid():
            m = fm.cleaned_data['Month']
            em = fm.cleaned_data['Day']
            pw = fm.cleaned_data['Expinc']
            dw = fm.cleaned_data['Tag']
            fw = fm.cleaned_data['Amount']
            reg = Uinput(Month=m, Day=em, Expinc=pw,Tag=dw,Amount=fw,user=request.user)
            reg.save()
            fm = Userentry()
    else:
        fm = Userentry()
    
    log_user = request.user
    stud = Uinput.objects.filter(user=log_user)
    myFilter = OrderFilter(request.GET, queryset=stud)
    
    stud = myFilter.qs
    return render(request,'entry.html',{'form':fm,'stu':stud,'myFilter': myFilter})

def analytics(request):
    log_user = request.user
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
    
    chart1 = get_plot(X,Y)
    chart2 = get_plot_pie(x1,y1)
    if request.POST.get('bar'):
        return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'chart':chart1})
    elif request.POST.get('pie'):
        return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'chart':chart2})
    else:
        return render(request,'Analytics.html',{'stu':stud_2,'myFilter': myFilter,'sum_income':int(sum_income['p1']),'sum_expense':int(sum_expense['p2']),'sum_diff':sum_diff,'s':"** please click on either 'Bar plot' button or 'Pie chart' button to see the respective graph **"})
