from django.db import models

# default models often used:

class Chat(models.Model):
    chat_id = models.BigIntegerField(primary_key=True)  # Telegram chat id
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    is_group = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Message(models.Model):
    message_id = models.BigIntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    from_bot = models.BooleanField(default=False)
    text = models.CharField(max_length=600, null=True, blank=True)
    author_id = models.BigIntegerField()
