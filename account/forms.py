from django.contrib.auth import get_user_model
from django import forms 
User = get_user_model()


class RegisterForm(forms.Form):
     username = forms.CharField()
     email = forms.EmailField()

    
     password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

     def clean_username(self):
        username=self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        
        if  qs.exists():
            raise forms.ValidationError("sorry this is not allowed.")
        
        return username
    
     def clean_email(self):
        email=self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        
        if not qs.exists():
            raise forms.ValidationError("sorry invalid user.")
        
        return email




class loginform(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    
    # def clean(self):
    #     username=self.cleaned_data.get('username')
    #     password=self.cleaned_data.get('password')
    
    
    
    
    
    def clean_username(self):
        username=self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        
        if not qs.exists():
            raise forms.ValidationError("sorry invalid user.")
        
        return username
    
    