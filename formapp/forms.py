from django import forms
from .models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
    fields=['firstname','lastname','username','password','cpassword','mailid','mobno']
    widgets={'password':forms.PasswordInput(),'cpassword':forms.PasswordInput()}
    firstname=forms.CharField(max_length=10)
    lastname=forms.CharField(max_length=10)
    username=forms.CharField(max_length=10)
    password=forms.CharField(max_length=10,widget=forms.PasswordInput())
    cpassword=forms.CharField(max_length=10,widget=forms.PasswordInput())
    mailid=forms.CharField()
    mobno=forms.IntegerField()
