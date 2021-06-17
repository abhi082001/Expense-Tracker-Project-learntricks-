from django import forms
from .models import Uinput

class Userentry_1(forms.ModelForm):
    class Meta:
        model = Uinput
        fields = ['Month','Day','Expinc','Tag','Amount']
        
        widgets = {
            
            'Amount': forms.NumberInput(attrs={'class':'form-control'}),
        }