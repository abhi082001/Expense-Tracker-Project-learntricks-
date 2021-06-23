import django_filters
from django_filters import FilterSet, ModelChoiceFilter
from .models import Uinput

class OrderFilter(django_filters.FilterSet):
    #student__nationality = ModelChoiceFilter(queryset=Uinput.Month.objects.all(), empty_label=('June'))

    class Meta:
        model = Uinput
        fields =  ['Month']
        
class OrderFilter1(django_filters.FilterSet):
    class Meta:
        model = Uinput
        fields = ['Month','Expinc']