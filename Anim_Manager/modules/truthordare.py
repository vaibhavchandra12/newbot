import html
import random
import Anim_Manager.modules.truth_and_dare_string as truth_and_dare_string
from Anim_Manager import dispatcher
from telegram import ParseMode, Update, Bot
from Anim_Manager.modules.disable import DisableAbleCommandHandler
from telegram.ext import run_async


@run_async
def truth(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.TRUTH))

@run_async
def dare(bot: Bot, update: Update):
    update.effective_message.reply_text(random.choice(truth_and_dare_string.DARE))


__help__ = """
 
 Lets Play Truth and Dare Game With Friends 
 
- /truth
- /dare
"""

TRUTH_HANDLER = DisableAbleCommandHandler("truth", truth)
DARE_HANDLER = DisableAbleCommandHandler("dare", dare)

dispatcher.add_handler(TRUTH_HANDLER)
dispatcher.add_handler(DARE_HANDLER)

__mod_name__ = "🆃 OR 🅳"
__command_list__ = ["truth", "dare"]
__handlers__ = [TRUTH_HANDLER, DARE_HANDLER]
