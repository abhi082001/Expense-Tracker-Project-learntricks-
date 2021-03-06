# Generated by Django 3.2.4 on 2021-06-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0006_tagtable_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uinput',
            name='Tag',
            field=models.CharField(choices=[('-', '-----Expense Choices-----'), ('House Rent', 'House Rent'), ('Grocery', 'Grocery'), ('Vegetables', 'Vegetables'), ('Fuel expenses', 'Fuel expenses'), ('Car loan', 'Car loan'), ('Housing loan', 'Housing loan'), ('Medical expenses', 'Medical expenses'), ('Electricity bill', 'Electricity bill'), ('Water bill', 'Water bill'), ('SIM card recharge', 'SIM card recharge'), ('Internet', 'Internet'), ('Cooking Gas', 'Cooking Gas'), ('School fees', 'School fees'), ('Transportation fees', 'Transportation fees'), ('Hostel fee', 'Hostel fee'), ('Bus pass', 'Bus pass'), ('Gym fee', 'Gym fee'), ('College fee', 'College fee'), ('Others', 'Others'), ('-', '-----Income Choices-----'), ('Salary', 'Salary'), ('FD Interest', 'FD Interest'), ('Part Time', 'Part Time'), ('Prize money', 'Prize money'), ('Freelancing', 'Freelancing'), ('House rent income', 'House rent income'), ('Bit coin', 'Bit coin'), ('Dividends income', 'Dividends income'), ('Side business', 'Side business'), ('Others', 'Others')], max_length=70),
        ),
    ]
