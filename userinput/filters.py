import django_filters

from .models import Uinput

class OrderFilter(django_filters.FilterSet):
    class Meta:
        model = Uinput
        fields = ['Month']