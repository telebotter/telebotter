from django import template
from django.utils.html import format_html
from django_telegram_login.widgets.generator import create_redirect_login_widget
from core.models import Bot

register = template.Library()


@register.inclusion_tag('core/card.html')
def as_card(data):
    """ generates a bootstrap card from dictionary
    """
    return data

@register.inclusion_tag('core/bot_card.html')
def as_bot_card(data):
    return data

@register.inclusion_tag('core/media.html')
def as_media(data):
    """ generates a bootstrap card from dictionary
    """
    return data

@register.simple_tag
def tg_login_widget():
    telegram_login_widget = create_redirect_login_widget('/login/verify', 'telebotterbot', size='medium', access_write=True)
    return format_html(telegram_login_widget)

@register.simple_tag
def get_bot_list():
    bots = Bot.objects.all()
    print('got bots: ', bots)
    return bots
