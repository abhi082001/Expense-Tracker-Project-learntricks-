from django.contrib import admin

# Register your models here.
from .models import amount_table
# Register your models here.
@admin.register(amount_table)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','month','date','Expinc','amount')