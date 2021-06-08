import logging


from telegram import Update, ForceReply, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, ConversationHandler
from telegram.vendor.ptb_urllib3.urllib3.contrib.socks import SOCKSProxyManager


# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M'


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
# def start(update, context):
#     """Send a message when the command /start is issued."""
#     update.message.reply_text('سلام مهدی خوبی دارم تست می‌کنم!')

def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'سلام {user.mention_markdown_v2()}\!',
        reply_markup=ForceReply(selective=True),
    )

def rollup(update: Update, _: CallbackContext) -> int:
    """Starts the conversation and asks the user about their gender."""
    reply_keyboard = [['Boy', 'Girl', 'Other']]

    update.message.reply_text(
        'سلام! شما با ربات مجموعه درب‌های اتوماتیک ویرا در حال مکالمه هستید. خوشحالیم از این‌که با ما هستید.. '
        'Send /cancel to stop talking to me.\n\n'
        'Are you a boy or a girl?',
        reply_markup=ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True),
    )

    return GENDER #errorrrrrrrrrrrrrr

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():

    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    # updater = Updater("1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M", use_context=True)
    
    # TOKEN='1258007118:AAEcye1ZFyIwn1BT9EdJ6Jo6cYNaQE4T11M'
    # REQUEST_KWARGS={
    # # "USERNAME:PASSWORD@" is optional, if you need authentication:
    # # 'proxy_url': 'http://84.54.82.173:3128/',
    # 'proxy_url': 'socks5://116.202.103.223:52433',
    # }

    REQUEST_KWARGS={
    'proxy_url': 'socks5h://127.0.0.1:9150',
    # Optional, if you need authentication:
    # 'urllib3_proxy_kwargs': {
    #     'assert_hostname': 'False',
    #     'cert_reqs': 'CERT_NONE'
    #     'username': 'user',
    #     'password': 'password'
    # }
    }
    # updater = Updater(token='YOUR_TOKEN', request_kwargs={
    # 'proxy_url': 'socks5://127.0.0.1:1080/'
    # })

    
    
    updater = Updater(TOKEN, request_kwargs=REQUEST_KWARGS)
    

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("rollup", rollup))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()