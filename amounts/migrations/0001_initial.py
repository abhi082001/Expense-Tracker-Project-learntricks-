# Generated by Django 3.2.4 on 2021-06-11 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='amount_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=100)),
                ('date', models.IntegerField()),
                ('Expinc', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('amount', models.IntegerField()),
            ],
        ),
    ]
