from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from application.forms import UserInfoForm
from application.models import UserRegistration
# Create your views here.




def register(request):
    registered = False
    if request.method == 'POST':
        user_info_form = UserInfoForm(request.POST or None)
        # user_form = UserRegistrationForm(request.POST or None, request.FILES or None)
        if user_info_form.is_valid():

            user_info_form.save()
            # user_form.save()
            registered = True

        else:
            print(user_info_form.errors)

    else:
        user_info_form = UserInfoForm()
        # user_form = UserRegistrationForm()
    return render(request,'app/college_form.html',{'user_info_form':user_info_form,'registered':registered})
