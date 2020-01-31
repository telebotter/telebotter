import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler, MessageHandler, CallbackQueryHandler
from telegram.ext import Filters
from django_telegrambot.apps import DjangoTelegramBot
from {{ app_name }}.constants import *
from {{ app_name }}.commands import start, stop, help
from {{ app_name }}.models import SSP
logger = logging.getLogger('django')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    logger.info("Loading handlers for wuerfeln")
    dp = DjangoTelegramBot.getDispatcher('examplebot')
    commands = [start, stop, help]
    for cmd in commands:
        pass_args = cmd.pass_args if hasattr(cmd, 'pass_args') else False
        name = cmd.command if hasattr(cmd, 'command') else cmd.__name__
        dp.add_handler(CommandHandler(name, cmd, pass_args=pass_args))
    dp.add_error_handler(error)
