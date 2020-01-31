from {{ app_name }}.constants import *


def start(bot, update):
    # get or create + logging
    update.message.reply_text(MESSAGES['start'])
start.short = 'Beginne die Unterhaltung'
start.long = 'Beginne die Unterhaltung /start oder durch Drücken des Start-Buttons. Wenn ich dich in Ruhe lassen soll /stop.'


def help(bot, update):
    """
    cmds = '\n'
    for cmd in commands:
        name = cmd.name if hasattr(cmd, 'name') else cmd.__name__
        desc = ' - {}'.format(cmd.short) if hasattr(cmd, 'short') else ''
        cmds += '`/'+name+'`' + desc + '\n'
    update.message.reply_text(MESSAGES['help'].format(cmds), parse_mode='Markdown')
    """
    update.message.reply_text(MESSAGES['help'], parse_mode='Markdown')
help.short = 'Hilfe und Befehle anzeigen'
help.long = 'Ich zeige dir wie du mit mir umgehen kannst.'


def stop(bot, update):
    update.message.reply_text(MESSAGES['stop'], parse_mode='Markdown')
help.short = 'Verbiete mir in diesen Chat zu schreiben'
help.long = 'Ich werde keine automatischen Nachrichten mehr schicken aber noch auf Befehle reagieren.'
