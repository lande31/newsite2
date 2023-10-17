from django import forms

from .models import item,Customer

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields= ('name','desc','price')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','phone','email','password')