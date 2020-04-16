import os
import logging
import logging.handlers
from telegram import ChatAction
from django.conf import settings
from functools import wraps
logger = logging.getLogger(__name__)


def dict_format(pattern, data):
    """The String.format(dict) method is used a lot to fill the answers.
    TODO: maybe use something like djangos rendering for this?
    this function can be imported as shortcut"""
    return pattern.format(data)


def quick_reply(update, text, **kwargs):
    kwargs['quote'] = kwargs.get('quote', False)
    kwargs['parse_mode'] = kwargs.get('parse_mode', 'HTML')
    update.effective_message.reply_text(text, **kwargs)


def send_action(action):
    """Sends `action` while processing func command.
    https://github.com/python-telegram-bot/python-telegram-bot/
    wiki/Code-snippets#send-action-while-handling-command-decorator
    Usage:
    ```
    @send_action(ChatAction.TYPING)
    def type_and_answer(update, context):
        ...
    ```
    or shortcuts:
    ```
    @typing_action
    def type_and_answer(update, context):
        ...
    ```
    """
    def decorator(func):
        @wraps(func)
        def command_func(update, context, *args, **kwargs):
            context.bot.send_chat_action(
                chat_id=update.effective_message.chat_id,
                action=action)
            return func(update, context,  *args, **kwargs)
        return command_func
    return decorator

# shortcuts for send_action without using any argument:
typing_action = send_action(ChatAction.TYPING)
upload_video_action = send_action(ChatAction.UPLOAD_VIDEO)
upload_photo_action = send_action(ChatAction.UPLOAD_PHOTO)


def restricted(func):
    """ decorator for handler function, that only allows admins (user ids in
    settings.ADMIN_LIST) to use this command.
    """
    @wraps(func)
    def wrapped(update, context, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in settings.ADMIN_LIST:
            logger.warning("Unauthorized access denied for {}.".format(user_id))
            return
        return func(update, context, *args, **kwargs)
    return wrapped


class GWTimedRotatingFileHandler(logging.handlers.TimedRotatingFileHandler):
    """ A modified TimedRotatingFileHandler to create new logfiles with write
    permission for groups. Based on this example from SO:
    https://stackoverflow.com/a/6779307/7268121
    """

    def _open(self):
        prevumask=os.umask(0o002)
        rtv=logging.handlers.TimedRotatingFileHandler._open(self)
        os.umask(prevumask)
        return rtv
