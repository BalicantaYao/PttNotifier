from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from .models import Subscrption, Board, BoardCategory, Notification
from django import forms
from django.http import Http404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django_ajax.decorators import ajax
import redis
import re
import logging
import base64
import json


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
def notification_list(request):
    notifications = Notification.objects.filter(user_id=request.user.id, is_read=False)
    return render(request, 'notification_list.html', {'notifications': notifications})


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


def _get_use_id_by_sessionid(session_id):
    redis_client = redis.StrictRedis(host='localhost', port=6379, db=1)
    session_content = redis_client.get('session:' + session_id)
    session_content = session_content.decode('utf-8')

    decoded_content = base64.standard_b64decode(session_content)
    decoded_content = str(decoded_content)

    p = re.compile('"_auth_user_id":(\d+),"')
    value = p.findall(decoded_content)
    try:
        return str(value[0])
    except IndexError:
        logging.error('Invalid user id.')
        return None


@ajax
def get_notifications_by_id_from_client(request):
    user_id = _get_use_id_by_sessionid(request.COOKIES['sessionid'])

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    byte_notifications = redis_client.hgetall(user_id)
    str_notifications = {k.decode('utf-8'): v.decode('utf-8') for k, v in byte_notifications.items()}
    json_notifications = json.dumps(str_notifications)
    # logging.info(str_notifications)

    return json_notifications


@ajax
def mark_as_read_and_del_in_redis_on_click(request):
    logging.info('got ajax post')
    post_dict = request.POST.dict()
    user_id = _get_use_id_by_sessionid(request.COOKIES['sessionid'])

    Notification.objects.filter(
        subscription_user__id=user_id,
        match_url=post_dict['url'],
        article_topic=post_dict['title']).update(is_read=True)

    redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
    redis_client.hdel(user_id, post_dict['url'])
    byte_notifications = redis_client.hgetall(user_id)
    str_notifications = {k.decode('utf-8'): v.decode('utf-8') for k, v in byte_notifications.items()}
    json_notifications = json.dumps(str_notifications)

    return json_notifications
