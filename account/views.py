from django.shortcuts import render,redirect
from .forms import loginform,RegisterForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.



def register_view(request):
   
    form=RegisterForm(request.POST or None)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        confirm_password=form.cleaned_data.get('confirm_password')
        
        
        user =authenticate(request,username=username,email=email,password=password,confirm_password=confirm_password)
        
        if user == None:
            # attempt = request.session.get("attempt") or 0 
            # request.session['attempt'] +=1
            
            return render(request,"register.html",{"form":form,"invalid_user":True})
        else:
        #   login(request,user)
             request.session["error"]
    
    return render(request,"register.html",{"form":form,"invalid_user":True})









def loginview(request):
    form=loginform(request.POST or None)
    
    if form.is_valid():
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        
        user =authenticate(request,username=username,password=password)
        
        if user == None:
            # attempt = request.session.get("attempt") or 0 
            # request.session['attempt'] +=1
            
            return render(request,"forms.html",{"form":form,"invalid_user":True})
        
        login(request,user)
        return redirect("/")
    
    return render(request,"forms.html",{"form":form,"invalid_user":True})

def logout_view(request):
    logout(request)
    messages.success(request,"you loged out successfully!")
    return render(request,'logout.html')