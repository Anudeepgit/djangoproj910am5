from django import forms
from .models import Reg
class RegForm(forms.ModelForm):
    class Meta:
        model=Reg
        widgets={'Pwd':forms.PasswordInput(),}
        fields=['User','Pwd','fname','lname','Dob','mobno']
class LoginForm(forms.Form):
    User=forms.CharField(max_length=20)
    Pwd=forms.CharField(widget=forms.PasswordInput())
