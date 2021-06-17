from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
Month_choices= (
    ('January','JANUARY'),
    ('February','FEBRUARY'),
    ('March', 'MARCH'),
    ('April','APRIL'),
    ('May','MAY'),
    ('June','JUNE'),
    ('July','JULY'),
    ('August','AUGUST'),
    ('September','SEPTEMBER'),
    ('October','OCTOBER'),
    ('November','NOVEMBER'),
    ('December','DECEMBER')
)
Day_choices =(
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
    (6,6),
    (7,7),
    (8,8),
    (9,9),
    (10,10),
    (11,11),
    (12,12),
    (13,13),
    (14,14),
    (15,15),
    (16,16),
    (17,17),
    (18,18),
    (19,19),
    (20,20),
    (21,21),
    (22,22),
    (23,23),
    (24,24),
    (25,25),
    (26,26),
    (27,27),
    (28,28),
    (29,29),
    (30,30),
    (31,31)
)

Exp_choices= (
    ('Expense','EXPENSE'),
    ('Income','INCOME')
)

Tag_choices =(
    ('-','-----Expense Choices-----'),
    ('House Rent','House Rent'),
    ('Grocery','Grocery'),
    ('Vegetables','Vegetables'),
    ('Fuel expenses','Fuel expenses'),
    ('Car loan','Car loan'),
    ('Housing loan','Housing loan'),
    ('Medical expenses','Medical expenses'),
    ('Electricity bill','Electricity bill'),
    ('Water bill','Water bill'),
    ('SIM card recharge', 'SIM card recharge'),
    ('Internet','Internet'),
    ('Cooking Gas','Cooking Gas'),
    ('School fees','School fees'),
    ('Transportation fees','Transportation fees'),
    ('Hostel fee','Hostel fee'),
    ('Bus pass','Bus pass'),
    ('Gym fee','Gym fee'),
    ('College fee','College fee'),
    ('Others','Others'),
    
    
    ('-','-----Income Choices-----'),
    ('Salary','Salary'),
    ('FD Interest','FD Interest'),
    ('Part Time', 'Part Time'),
    ('Prize money','Prize money'),
    ('Freelancing', 'Freelancing'),
    ('House rent income','House rent income'),
    ('Bit coin','Bit coin'),
    ('Dividends income','Dividends income'),
    ('Side business','Side business'),
    ('Others','Others')
)

class Uinput(models.Model):
    Month = models.CharField(max_length=70, choices = Month_choices)
    Day = models.IntegerField(choices = Day_choices)
    Expinc = models.CharField(max_length=70,choices = Exp_choices)
    Tag = models.CharField(max_length=70,choices = Tag_choices)
    Amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete = models.CASCADE)

class exptable(models.Model):
    Pid = models.IntegerField(primary_key = True)
    Ename = models.CharField(max_length = 70)

class tagtable(models.Model):
    ID = models.IntegerField(primary_key = True)
    tagname = models.CharField(max_length = 70)
    Pid = models.IntegerField()

class tagtable_income(models.Model):
    ID_1 = models.IntegerField(primary_key = True)
    tagname_1 = models.CharField(max_length = 70)
    Pid_1 = models.IntegerField()

