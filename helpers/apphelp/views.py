from django.shortcuts import render
from apphelp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse
import base64
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
from django.conf import settings 
from django.shortcuts import redirect

import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
from tensorflow.python.keras.backend import set_session
import tensorflow.compat.v1 as tf
import numpy as np
import traceback
from . import predict



def index(request):
    return render(request,'apphelp/index.html')
@login_required
def special(request):
    return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'apphelp/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'apphelp/login.html', {})


from apphelp.models import UserProfileInfo
from django.contrib.auth.models import User

def leaderboard(request):

    top10 = (UserProfileInfo.objects.values_list('user_id', 'points').order_by('points'))[:2]
    name=[]
    points=[]
    tuplist =[]
    i=1
    for user_id_main, score in top10:
        user = (User.objects.filter(id = user_id_main).values('username'))[0]
        tuplist.append((i,user['username'],score))
        i+=1


    return render(request, 'apphelp/leaderboard.html', {'tuplist': tuplist})

def donate(request):
    if  request.method == "POST":
        f=request.FILES['sentFile'] # here you get the files needed
        response = {}
        label, category = predict.predict(f)

        response['name'] = str(category)
        tf.keras.backend.clear_session()
        
        return render(request,'apphelp/donate.html',response)

    else:
        return render(request,'apphelp/donate.html')

    # return render(request, 'apphelp/donate.html')
