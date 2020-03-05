from telegram import TelegramError, Update
from telegram.ext import CommandHandler, CallbackContext, Filters, run_async

from tg_bot import dispatcher, DEV_USERS

@run_async
def leave(update: Update, context: CallbackContext):

    args = context.args
    bot = context.bot

    if args:
        chat_id = str(args[0])
        try:
            bot.leave_chat(int(chat_id))
            update.effective_message.reply_text("Beep boop, I left that soup!.")
        except TelegramError:
            update.effective_message.reply_text("Beep boop, I could not leave that group(dunno why tho).")
    else:
        update.effective_message.reply_text("Send a valid chat ID") 

LEAVE_HANDLER = CommandHandler("leave", leave, filters=Filters.user(DEV_USERS))
dispatcher.add_handler(LEAVE_HANDLER)

__mod_name__ = "Leave"
