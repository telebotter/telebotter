from django.shortcuts import render
from core.models import Bot
import random

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
