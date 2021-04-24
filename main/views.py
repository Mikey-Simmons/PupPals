from django.shortcuts import render

from django.shortcuts import render, HttpResponse, redirect
from .models import  User 
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request,'index.html')
def registration(request):
    return render(request, 'register.html')
def login(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/') 
    list_of_users = User.objects.filter(email=request.POST['email'])
    if len(list_of_users) > 0:
        user = list_of_users[0]
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            request.session['user_id'] = user.id
            print('login successful')
            return redirect('/welcome')
    #logic for logging in


    return redirect('/')
def welcome(request):
    if 'user_id' in request.session:
        logged_in_user = User.objects.get(id=request.session['user_id'])
        all_users = User.objects.all()
        context = {
        'logged_in_user': logged_in_user,
        'all_users' : all_users
         }
        return render(request,'welcome.html',context)
    else:
        return redirect('/')
    #If a login is succesful it will redirect user to the main home page
def register(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors)>0:
        for key,value in errors.items():
            messages.error(request,value)
        return redirect('/signup')
    else:
        password=request.POST['password']
        pw_hash = bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()
        new_user = User.objects.create(
        dog_name = request.POST['dog_name'],
        dog_gender= request.POST['dog_gender'],
        dog_breed= request.POST['dog_breed'],
        dog_weight= request.POST['dog_weight'],
        dog_age= request.POST['dog_age'],
        dog_city= request.POST['dog_city'],
        dog_state= request.POST['dog_state'],
        dog_owner_first= request.POST['dog_owner_first'],
        dog_owner_last= request.POST['dog_owner_last'],
        email = request.POST['email'],
        password = pw_hash
    )
    messages.success(request,"User Successfully created!")
    request.session['user_id'] = new_user.id
    return redirect('/welcome')
def logout(request):
    request.session.clear()
    return redirect('/')