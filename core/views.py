from django.shortcuts import render
from core.models import Bot
import random
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from core.models import TelebotUser
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login

from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import (
    NotTelegramDataError,
    TelegramDataIsOutdatedError,
)
from django_telegram_login.widgets.constants import LARGE
from django_telegram_login.widgets.generator import create_redirect_login_widget


# Create your views here.
def index(request):
    context = {}
    bots = Bot.objects.all()
    context['bot_cnt'] = bots.count()
    context['promos'] = bots.filter(promote=True).order_by('?')[:3]
    return render(request, 'core/index.html', context)


def botlist(request):
    context = {}
    context['bots'] = Bot.objects.filter(public=True)
    return render(request, 'core/botlist.html', context)

def botinfo(request, appname):
    bot = Bot.objects.get(appname=appname)
    messages.info(request, 'Diese Seite ist automatisch generiert worden. Es wurden noch keine Infoseiten eingetragen.')
    return render(request, 'core/botinfo.html', {'bot': bot})

def tglogin(request):
    telegram_login_widget = create_redirect_login_widget('/login/verify', 'telebotterbot', size='medium', access_write=True)
    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'core/login.html', context)


def tglogin_verify(request):
    # Initially, the index page may have no get params in URL
    # For example, if it is a home page, a user should be redirected from the widget
    if not request.GET.get('hash'):
        messages.error(request, 'Missing telegram data.')
        return HttpResponseRedirect('/login')

    try:
        bot_token = settings.TELEBOTTER_BOT_TOKEN
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

    except TelegramDataIsOutdatedError:
        messages.error(request, 'The authentication data was received more than a day ago.')
        return HttpResponseRedirect('/login')

    except NotTelegramDataError:
        messages.error(request, 'The data is not related to the Telegram user!')
        return HttpResponseRedirect('/login')

    # user verified by telegram:
    # find the telebotter user (settings) and related django user (auth)
    tuser, tnew = TelebotUser.objects.get_or_create(pk=result['id'], defaults=result)
    if tnew:
        messages.success(request, "Neuen Telebotter Nutzer registriert.")
    else:
        messages.success(request, "Telebotter Nutzer erkannt")
    if not tuser.django_user:
        messages.warning(request, "(Noch) kein django user verknüpft.")
        # TODO create django user
        duser = User.objects.create_user(username=str(result['id']), password=None, email=None)
        messages.info(request, "Django user ohne password erstellt")
        tuser.django_user = duser
    else:
        duser = tuser.django_user
    login(request, duser)
    if duser.is_authenticated:
        messages.success(request, "Du bist erfolgreich eingeloggt")
    # Todo: only save if any of above changed?
    tuser.save()
    # duser, new = User.objects.get_or_create()
    return HttpResponseRedirect('/')
