from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Subscrption, User
from django.forms.models import modelform_factory
from django.http import Http404

# Create your views here.


def home(request):
    # return render(request, 'home.html')
    context = RequestContext(request,
                             {'request': request,
                              'user': request.user})
    return render_to_response('home.html',
                              context_instance=context)


def subscription_list(request):
    # User.object
    # subscriptions = Subscrption.objects.all()
    subscriptions = Subscrption.objects.filter(user_id=request.user.id)
    return render(
        request, 'subscription_list.html', {'subscriptions': subscriptions})


def subscription_detail(request, pk):
    try:
        subscription = Subscrption.objects.get(pk=pk)
    except Subscrption.DoesNotExist:
        raise Http404
    return render(
        request, 'subscription_detail.html', {'subscription': subscription})


def subscription_create(request):
    # SubscriptionFrom = modelform_factory(
    #     Subscrption, fields=('user', 'keywords'))

    # if request.method == 'POST':
    #     form = SubscriptionFrom(request.POST)

    #     if form.is_valid():
    #         subscription = form.save()
    #         return redirect(subscription.get_absolute_url())
    # else:
    #     form = SubscriptionFrom()

    return render(
        request, 'subscription_create.html', {})
    # return redirect(subscription_create)

def subscription_insert(request):
    s = get_object_or_404(User, pk=request.user.id)

    SubscriptionFrom = modelform_factory(
        Subscrption, fields=('user', 'keywords'))
    form = SubscriptionFrom(request.user.id, request.POST["subscribe_keywords"])
    # form.user_id = request.user.id

    # raise Exception(form)

    subscription = form.save()
    return redirect(subscription.get_absolute_url())
