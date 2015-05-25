#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: bustta
# @Date:   2015-05-26 00:10:17
# @Last Modified by:   bustta
# @Last Modified time: 2015-05-26 00:14:17

from django.contrib import auth
from django.shortcuts import redirect, render_to_response

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
