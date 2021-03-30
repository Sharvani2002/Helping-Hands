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


from apphelp.models import UserProfileInfo
from django.contrib.auth.models import User

def index(request):
    # if 'is_private' in request.POST:
    #     is_private = request.POST['is_private']
    # else:
    #     is_private = False
    # user_id = request.POST.get('id')
    # if (request.user.is_authenticated):
    if (request.user.id):   
        user_id = request.user.id
        pts=0
        try:
            if(request.user.id):
                a = UserProfileInfo.objects.get(user_id = user_id)
                pts  = a.points
            # pts = request.user.points
                return render(request,'apphelp/index.html',{'points':pts})
        except:
            return render(request,'apphelp/index.html',{})
    else:
        return render(request,'apphelp/index.html',{})

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
                return HttpResponseRedirect(reverse('index'), {})
            else:
                return HttpResponse("Your account was inactive.", {})
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'apphelp/login.html', {})



def leaderboard(request):

    response = {}
    if (request.user.id):   
        user_id = request.user.id
        pts=0
        try:
            if(request.user.id):
                a = UserProfileInfo.objects.get(user_id = user_id)
                response['points']= a.points

        except:
            response['points']= pts
    top10 = (UserProfileInfo.objects.values_list('user_id', 'points').order_by('-points'))[:10]
    name=[]
    points=[]
    tuplist =[]
    i=1
    for user_id_main, score in top10:
        user = (User.objects.filter(id = user_id_main).values('username'))[0]
        tuplist.append((i,user['username'],score))
        i+=1
    response['tuplist']=tuplist


    return render(request, 'apphelp/leaderboard.html', response)

from django.core.files.storage import FileSystemStorage

def donate(request):
    response = {}
    if (request.user.id):   
        pts=0
        try:
            if(request.user.id):
                a = UserProfileInfo.objects.get(user_id = request.user.id)
                response['points']= a.points
        except:
            response['points']= pts


    if  request.method == "POST":
        f=request.FILES['sentFile'] # here you get the files needed
        label, category = predict.predict(f)
        response['name'] = str(category)
        tf.keras.backend.clear_session()
        
        response['d_img'] =''
        if(str(category)!='Glass' or str(category)!='Metal'):
            response['valid'] = 1
            # instance=request.user
            user_id = request.POST.get('id')
            a = UserProfileInfo.objects.get(user_id = user_id)
            a.points += 10
            from django.core.files.storage import default_storage
            file = f
            extension = file.name.split('.')[1]
            ffnn = str("user_id_"+str(user_id)+"_"+str(int(a.points/10))+str('.')+str(extension))
            # file_name = default_storage.save(ffnn, file)
            try:
                folder=os.path.join(settings.STATIC_DIR, "donations")
            except:
                folder=settings.STATIC_DIR

            fs = FileSystemStorage(location=folder) #defaults to   MEDIA_ROOT  
            filename = fs.save(ffnn, f)
            file_url = fs.url(filename)
            file_html_url = os.path.join("donations",ffnn)
            a.save()
            response['user_id']=user_id
            response['points']= a.points

            if(a.points>0):
                response['d_img'] = file_url
                response['d_static']=file_html_url
            #  Reading file from storage
            # file = default_storage.open(file_name)

        else:
            response['valid'] = 0
            response['d_static']='donations/user_id_5_15.jpg'

            
        return render(request,'apphelp/donate.html',response)

    else:
        return render(request,'apphelp/donate.html')

