from django.contrib import admin

# Register your models here.
from .models import Uinput,exptable,tagtable
# Register your models here.

admin.site.register(Uinput)
admin.site.register(exptable)
admin.site.register(tagtable)