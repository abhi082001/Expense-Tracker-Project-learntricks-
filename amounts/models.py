from django.db import models

# Create your models here.
class amount_table(models.Model):
    month = models.CharField(max_length = 100)
    date = models.IntegerField()
    Expinc = models.CharField(max_length = 100)
    tags = models.CharField(max_length = 100)
    amount = models.IntegerField()
