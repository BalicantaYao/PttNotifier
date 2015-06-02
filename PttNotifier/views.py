#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-05-26 00:10:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-05-26 00:14:17

from django.contrib import auth
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


def home(request):
    context = RequestContext(request, {'request': request, 'user': request.user})
    return render_to_response('home.html', context_instance=context)


def contact(request):
    return render(request, 'contact.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def comments(request):
    return render(request, 'comments.html', {})


def terms_and_condictions(request):
    return render(request, 'terms_and_condictions.html', {})


class RegistrationForm(UserCreationForm):
    # username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=75)

    class Meta:
        model = User
        fields = ['email', ]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data["username"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm(request.POST)
    c = {'form': form}
    return render_to_response('registration/register.html', c, context_instance=RequestContext(request))


def login(request):
    if request.user.is_authenticated():
        return redirect('home')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(usernae=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return redirect('home')
    else:
        return render_to_response('login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')
