# Generated by Django 3.2.4 on 2021-06-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinput', '0007_alter_uinput_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uinput',
            name='Day',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20), (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27), (28, 28), (29, 29), (30, 30), (31, 31)], default=29),
        ),
        migrations.AlterField(
            model_name='uinput',
            name='Month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='June', max_length=70),
        ),
    ]
