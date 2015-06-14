from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import UserProfile
from django import forms


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['substituted_mail', ]


@login_required
def profile(request):
    user_profile = UserProfile.objects.get_or_create(user_id=request.user.id)[0]
    if not user_profile.substituted_mail:
        user_profile.substituted_mail = User.objects.get(pk=request.user.id).email

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'user_profile': user_profile})
