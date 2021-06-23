from django import forms
from .models import Uinput

class Userentry(forms.ModelForm):
    class Meta:
        model = Uinput
        fields = ['Amount']
        
        widgets = {
            
            'Amount': forms.NumberInput(attrs={'class':'form-control'}),
        }
        
