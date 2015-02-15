from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Subscrption
from django import forms
from django.http import Http404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    # return render(request, 'home.html')
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)


def contact(request):
    return render(request, 'contact.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})

@login_required
def subscription_list(request):
    subscriptions = Subscrption.objects.filter(user_id=request.user.id)
    return render(
        request, 'subscription_list.html', {'subscriptions': subscriptions})


@login_required
def subscription_detail(request, pk):
    try:
        subscription = Subscrption.objects.get(pk=pk)
    except Subscrption.DoesNotExist:
        raise Http404
    return render(
        request, 'subscription_detail.html', {'subscription': subscription})


class SubscriptionForm(forms.ModelForm):
        class Meta:
            model = Subscrption
            fields = ['user', 'keywords', ]

@login_required
def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            new_subscription = form.save()
            # return redirect(new_subscription.get_absolute_url())
            return redirect('subscription_list')
    form = SubscriptionForm()
    return render(request, 'subscription_create.html', {'form': form})

@login_required
def subscription_update(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            new_subscription = form.save()
            # return redirect(new_subscription.get_absolute_url())
            return redirect('subscription_list')
    return render(request, 'subscription_update.html', {'subscription': subscription})


@login_required
def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    if (subscription.user_id == request.user.id):
        subscription.delete()
        return redirect('subscription_list')
    return HttpResponseForbidden()


@login_required
def subscription_delete_confirm(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    if (subscription.user_id == request.user.id):
        if request.method == 'POST':
            return subscription_delete(request, subscription.id)
        return render(
            request, 'delete_confirm.html',
            {'subscription': subscription})
    return HttpResponseForbidden()


