from django.shortcuts import render
from .forms import Userentry
from .models import Uinput
from django.contrib.auth.models import User, auth
from .filters import OrderFilter
from django.db.models import Sum

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
    sum_income = stud_1.aggregate(Sum('Amount'))
    stud_2 = stud.filter(Expinc = 'Expense')
    sum_expense = stud_2.aggregate(Sum('Amount'))
    
    return render(request,'Analytics.html',{'stu':stud_1,'myFilter': myFilter,'sum_income':sum_income,'sum_expense':sum_expense})

    
