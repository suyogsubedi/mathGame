from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import EmailInput, TextInput


"""
    Inheriting from from UserCreationForm
    This form is used to register a new user
""" 
class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=75,widget=TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=75,widget=TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name','last_name','email','password1','password2')
    
    def __init__(self,*args,**kwargs):
        super(RegisterUserForm,self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class']= 'form-control'
        self.fields['password1'].widget.attrs['class']= 'form-control'
        self.fields['password2'].widget.attrs['class']= 'form-control'