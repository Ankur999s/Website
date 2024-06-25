from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User  
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from datetime import datetime
from app.models import Contact

# Create your views here.
def home(request):
  
    return render(request , 'home.html')




def loginpage(request):
    if request.method=='POST':
        username = request.POST.get('username')
        pass1= request.POST.get('pass')
        user = authenticate(request, username = username, password=pass1)
        
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
         messages.error(request, "Username amd password incorect!")
        
    return render(request , 'login.html')

def signup(request):
    if request.method=="POST":
        username = request.POST.get('username')
        Email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        
        if pass1!=pass2:
            return HttpResponse("Password doesn't match")
        user =User.objects.create_user(username,Email,pass1)
        user.save()
        return redirect ('login')
    return render(request , 'signup.html')

def logoutpage(request):
    logout(request)
    return redirect("/")

def aboutus(request):
    return render(request , 'aboutus.html')

def contact(request):
     if request.method=="POST":
        name1= request.POST.get('name1')
        email1 = request.POST.get('email1')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name1=name1, email1=email1, phone=phone, desc=desc, date= datetime.today())
        contact.save()
     return render(request , 'contact.html')

def upd_prof(request):
    if request.method=="POST":
      first_name = request.POST.get('first_name')
      last_name = request.POST.get('last_name')
      username = request.POST.get('username')
      email = request.POST.get('email')
      bio = request.POST.get('bio')
      user_id = request.user.id
      
      user = User.objects.get(id=user_id)
      user.first_name = first_name
      user.last_name = last_name
      user.username = username
      user.email = email
      user.bio = bio
      user.save()
      messages.success(request,'Profile Are Succesfully Updated')
    return redirect('profile')
      
      
      
  
   
def profile(request):
  
    return render(request , 'profile.html')

def courses(request):
  
    return render(request , 'courses.html')

def changepass(request):
    if request.method =="POST":
     currentpassword = request.POST.get('currentpassword')
     newpassword = request.POST.get('newpassword')
     confirmpassword = request.POST.get('confirmpassword')
     user_id = request.user.id
     
     user = User.objects.get(id=user_id)
     user.currentpassword = currentpassword 
     user.password = newpassword
     user.confirmpassword = confirmpassword
     if newpassword == confirmpassword:
        user.set_password(newpassword) 
        user.save()
  
    return render(request , 'changepass.html')