# Generated by Django 3.2.4 on 2021-06-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0003_alter_uinput_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uinput',
            name='Month',
            field=models.CharField(choices=[('January', 'JANUARY'), ('February', 'FEBRUARY'), ('March', 'MARCH'), ('April', 'APRIL'), ('May', 'MAY'), ('June', 'JUNE'), ('July', 'JULY'), ('August', 'AUGUST'), ('September', 'SEPTEMBER'), ('October', 'OCTOBER'), ('November', 'NOVEMBER'), ('December', 'DECEMBER')], max_length=70),
        ),
    ]