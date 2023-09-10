import datetime
from django import forms
from django.core.validators import RegexValidator

phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")

class ClientForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField() 
    phoneNumber = forms.CharField(validators = [phoneNumberRegex], max_length = 16)
    adress = forms.CharField(max_length=200)
    date_regist = forms.DateField(initial=datetime.date.today, widget=forms.DateInput
                                (attrs={'class': 'form-control','type': 'date'}))
    
   
class ProductForm(forms.Form):
    name = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    quantity = forms.IntegerField()
    date_add = forms.DateField(initial=datetime.date.today, widget=forms.DateInput
                                (attrs={'class': 'form-control','type': 'date'}))
    image = forms.ImageField()
    

   