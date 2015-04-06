from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm


# Create your views here.
@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    return render(request, 'user_profile.html', {'user': user})
