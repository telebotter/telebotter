from django.shortcuts import render
from core.models import Bot
import random
from django.conf import settings
from django.http import HttpResponse


from django_telegram_login.authentication import verify_telegram_authentication
from django_telegram_login.errors import (
    NotTelegramDataError,
    TelegramDataIsOutdatedError,
)
from django_telegram_login.widgets.constants import (
    SMALL,
    MEDIUM,
    LARGE,
    DISABLE_USER_PHOTO,
)
from django_telegram_login.widgets.generator import (
    create_callback_login_widget,
    create_redirect_login_widget,
)


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


def tglogin(request):
    telegram_login_widget = create_redirect_login_widget('/tglogin/verify', 'telebotterbot', size=SMALL, access_write=True)
    context = {'telegram_login_widget': telegram_login_widget}
    return render(request, 'core/tglogin.html', context)


def tglogin_verify(request):
    # Initially, the index page may have no get params in URL
    # For example, if it is a home page, a user should be redirected from the widget
    if not request.GET.get('hash'):
        return HttpResponse('Handle the missing Telegram data in the response.')

    try:
        bot_token = settings.TELEBOTTER_BOT_TOKEN
        result = verify_telegram_authentication(bot_token=bot_token, request_data=request.GET)

    except TelegramDataIsOutdatedError:
        return HttpResponse('The authentication data was received more than a day ago.')

    except NotTelegramDataError:
        return HttpResponse('The data is not related to the Telegram user!')

    # Or handle it as you wish. For instance, save to the database.
    return HttpResponse('Hello, ' + result['first_name'] + '!')
