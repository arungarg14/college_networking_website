from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import TemplateView, ListView
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from application.forms import UserInfoForm, UserUpdateForm, ProfileUpdateForm
from application.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin


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



@login_required
def profile(request):
    return render(request, 'app/profile.html', {})

@login_required
def update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)


    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'app/update_info.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            # messages.success(request, f'Your password has been updated!')
            return redirect('profile')

    else:
        form = PasswordChangeForm(user=request.user)

    return render(request, 'app/password_change.html', {'form':form})


class ProfileListView(LoginRequiredMixin, ListView):
    model = User
    paginate_by = 5
    template_name = 'app/profile_list.html'
    def get_queryset(self):
        # return User.objects.filter().order_by('username')
        queryset = super(ProfileListView, self).get_queryset()
        queryset = queryset.order_by('username')
        return queryset
