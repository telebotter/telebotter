from django.contrib import admin
from core.models import Bot, TelebotUser
# Register your models here.

# placeholder to modify later
class BotAdmin(admin.ModelAdmin):
    pass
admin.site.register(Bot, BotAdmin)


class TelebotUserAdmin(admin.ModelAdmin):
    pass
admin.site.register(TelebotUser, TelebotUserAdmin)
