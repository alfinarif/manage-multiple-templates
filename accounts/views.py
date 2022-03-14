from django.shortcuts import render, redirect
from django.urls import reverse
import os
import random
from django.http import HttpResponseRedirect
from accounts.forms import RegisterForm
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

from accounts.models import User, Verification


class RegisterTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()

        context = {
            'form': form
        }
        return render(request, 'account/register.html', context)


    def post(self, request, *args, **kwargs):
        form = RegisterForm()
        if request.method == 'post' or request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save()
                    get_user_verification_obj = user.verification
                    acc_code = get_user_verification_obj.account_code
                    return redirect(reverse('accounts:verify', kwargs={'account_code': acc_code}))
                except:
                    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        context = {'form': form}
        return render(request, 'account/register.html', context)


def account_verification(request, account_code):
    try:
        get_user = User.objects.get(verification__account_code=account_code)
        get_code = get_user.verification.verify_code
        if request.method == 'post' or request.method == 'POST':
            check_code = request.POST.get('code')
            if get_code == check_code:
                get_user.is_active = True
                get_user.is_verify = True
                get_user.save()
                return redirect('accounts:login')
            else:
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

        context = {}
        return render(request, 'account/verification.html', context)
    except:
        return render(request, 'account/verification.html')



class LoginTemplateView(TemplateView):
    def get(self, request, *args, **kwargs):
        
        return render(request, 'account/login.html')

    def post(self, request, *args, **kwargs):
        if request.method == 'post' or request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
        return render(request, 'account/login.html')



