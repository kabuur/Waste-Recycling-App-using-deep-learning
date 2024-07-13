import warnings

warnings.filterwarnings('ignore')


from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import User_info
# Create your views here.



def Regestration(Request):
    massage = ""
    if Request.method == "POST":
        userName = Request.POST.get('userName')
   
        email = Request.POST.get('email')
        tell = Request.POST.get('tell')
        password1 = Request.POST.get('password1') 
        password2 = Request.POST.get('password2') 
        address = Request.POST.get('address')
        if(User.objects.filter(username = userName)):
                massage = "this user name "+ userName+ " is allready exist"
                return render(Request, 'registration/reg.html',{"massage": massage},)
        if password1!= password2:
             massage = "password must be same"
             return render(Request, 'registration/reg.html',{"massage": massage},)
        else:
           
        
                my_user = User.objects.create_user(username = userName, password=password1)
                my_user.save()
                
                user = User.objects.get(username =userName )
                
                print(user)
                
                create_user = User_info.objects.create(
                     
                        userName = user,
                        tell = tell,
                        email = email,
                        address  = address
                        
                )
                create_user.save()
                return redirect('/login')
  
    return render(Request, 'registration/reg.html',{"massage": massage},)



