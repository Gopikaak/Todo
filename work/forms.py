from django import forms
from work.models import User,Taskmodel

class Register(forms.ModelForm):
    
    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password"]
        widgets={
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'})
        }

class Taskform(forms.ModelForm):
    
    class Meta:
        model=Taskmodel
        fields=["task_name","task_discription"]
        widgets={
            'task_name':forms.TextInput(attrs={'class':'form-control','placeholder':'enter the task'}),
            'task_discription':forms.Textarea(attrs={'class':'form-control','column':20,'rows':5,'placeholder':'enter the description'})
        }
        

class Loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()