from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

# Create your views here.
def register_user(request):
    data = {}
    if request.method == "POST":
        uname = request.POST['username']
        upass = request.POST['password']
        uconf_pass = request.POST['password2']

        if(uname == '' or upass == '' or uconf_pass == ''):
            data['error_msg']='Fields cannot be empty'
            return render(request,'myapp/register.html',context=data)
        
        elif(upass!=uconf_pass):
            data['error_msg']='Password doesnt match'
            return render(request,'myapp/register.html',context=data)
        
        elif(User.objects.filter(username=uname).exists()):
            data['error_msg']= 'user: '+uname+' already exists!'
            return render(request,'myapp/register.html',context=data)
        
        else:
            user = User.objects.create(username=uname)
            user.set_password(upass)
            user.save()
            return HttpResponse("Registration Done!")
        
    return render(request,'myapp/register.html')

def login_user(request):
    data = {}
    if request.method=="POST":
        uname = request.POST['username']
        upass = request.POST['password']
        #implementing validation

        if(uname=='' or upass==''):
            data['error_msg']='Fields cant be empty'
            return render(request,'myapp/login.html',context=data)
        
        elif(not User.objects.filter(username=uname).exists()):
            data['error_msg']=uname+' user is not registered'
            return render(request,'myapp/login.html',context=data)
        
        else:
            user = authenticate(username=uname, password=upass)
            print(user)
            if user is not None:
                return redirect('/myapp/home')
            else:
                data['error_msg']='Wrong Password'
                return render(request,'myapp/login.html',context=data)
    return render(request,'myapp/login.html')

def home(request):
    return render(request,'myapp/home.html')