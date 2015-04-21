from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Subscrption, Board, BoardCategory
from django import forms
from django.http import Http404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax


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


def comments(request):
    return render(request, 'comments.html', {})


def terms_and_condictions(request):
    return render(request, 'terms_and_condictions.html', {})


@login_required
def subscription_list(request):
    subscriptions = Subscrption.objects.filter(user_id=request.user.id)
    for item in subscriptions:
        item.board = Board.objects.get(id=item.board_id)
        item.category = BoardCategory.objects.get(id=item.board.category_id)
        # print(board.board_cht_name)
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
        fields = ['user', 'keywords', 'board', ]

    def clean_keywords(self):
        data = self.cleaned_data['keywords']
        return data.replace(' ', '')


@login_required
def subscription_create(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('subscription_list')

    form = SubscriptionForm()
    board = Board.objects.all()
    board_category = BoardCategory.objects.all()

    return render(
        request,
        'subscription_create.html',
        {'form': form, 'board': board, 'board_category': board_category})


@login_required
def subscription_update(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    board = Board.objects.all()
    subscription.category_id = Board.objects.get(pk=subscription.board_id).category_id
    board_category = BoardCategory.objects.all()

    if request.method == 'POST':
        form = SubscriptionForm(request.POST, instance=subscription)
        if form.is_valid():
            form.save()
            # new_subscription = form.save()
            # return redirect(new_subscription.get_absolute_url())
            return redirect('subscription_list')
    return render(
        request,
        'subscription_update.html',
        {'subscription': subscription, 'board': board, 'board_category': board_category})


@login_required
def subscription_delete(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    if subscription.user_id == request.user.id:
        subscription.delete()
        return redirect('subscription_list')
    return HttpResponseForbidden()


@login_required
def subscription_delete_confirm(request, pk):
    subscription = get_object_or_404(Subscrption, pk=pk)
    if subscription.user_id == request.user.id:
        if request.method == 'POST':
            return subscription_delete(request, subscription.id)
        return render(
            request, 'delete_confirm.html',
            {'subscription': subscription})
    return HttpResponseForbidden()


@ajax
def get_notifications_by_id_from_client(request, pk):
    data = {'msg': 'HelloFromBackend.'}
    return data
