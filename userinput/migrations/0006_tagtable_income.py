# Generated by Django 3.2.4 on 2021-06-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0005_exptable_tagtable'),
    ]

    operations = [
        migrations.CreateModel(
            name='tagtable_income',
            fields=[
                ('ID_1', models.IntegerField(primary_key=True, serialize=False)),
                ('tagname_1', models.CharField(max_length=70)),
                ('Pid_1', models.IntegerField()),
            ],
        ),
    ]