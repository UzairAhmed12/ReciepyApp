from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def reciepes(request):  # sourcery skip: extract-method
    if request.method == "POST":
        data= request.POST
        reciepy_image = request.FILES.get("reciepy_image")
        reciepy_name = data.get("reciepy_name")
        reciepe_description = data.get('reciepe_description', "").strip()


        

        Reciepe.objects.create(
        reciepy_image = reciepy_image,
        reciepy_name = reciepy_name,
        reciepe_description = reciepe_description,  
        )

        
        return redirect('/reciepes/')
    queryset = Reciepe.objects.all()

    
    if request.GET.get('search'):
        queryset=queryset.filter(reciepy_name__icontains=request.GET.get('search'))

    context = {'receipes': queryset}

    return render(request, 'reciepes.html',context)

@login_required(login_url='/login/')
def update_reciepe(request, id):
    queryset = Reciepe.objects.get(id=id)

    if request.method=="POST":
        data=request.POST

        reciepy_image = request.FILES.get("reciepy_image")
        reciepy_name = data.get("reciepy_name")
        reciepe_description = data.get('reciepe_description', "").strip()

        queryset.reciepy_name=reciepy_name
        queryset.reciepe_description=reciepe_description

        if reciepy_image:
            queryset.reciepy_image=reciepy_image

        queryset.save()
        return redirect('/reciepes/')

    context = {'receipe': queryset}

    return render(request, "update_receipes.html", context)


@login_required(login_url='/login/')   
def delete_reciepe(request, id):
    queryset = Reciepe.objects.get(id=id)
    queryset.delete()
    return redirect('/reciepes/')
    
def login_page(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request, 'Invalid username')
            return redirect('/login/')
        
        user=authenticate(username=username, password=password)

        if user is None:
            messages.info(request, 'Invalid password')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/reciepes/')

        
    return render(request, 'login.html')
def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/register/')
            


        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
            

        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account Created Successfully')

        return redirect('/register/')
    return render(request, 'register.html')