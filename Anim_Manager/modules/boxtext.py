from typing import List
 
from telegram import Bot, Update
from telegram.ext import run_async, Filters
 
from Anim_Manager import dispatcher
from Anim_Manager.modules.disable import DisableAbleCommandHandler
 
normiefont = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
boxfont = ['🅰','🅱','🅲','🅳','🅴','🅵','🅶','🅷','🅸','🅹','🅺','🅻','🅼','🅽','🅾','🅿','🆀','🆁','🆂','🆃','🆄','🆅','🆆','🆇','🆈','🆉']
 
@run_async
def box(bot: Bot, update: Update, args: List[str]):
 
	string = '  '.join(args).lower()
	for normiecharacter in string:
		if normiecharacter in normiefont:
			boxcharacter = boxfont[normiefont.index(normiecharacter)]
			string = string.replace(normiecharacter, boxcharacter)
 
	message = update.effective_message
	if message.reply_to_message:
		message.reply_to_message.reply_text(string)
	else:
		message.reply_text(string)
 
 
__help__ = """
 - /box <text>: returns a box text
 - /mts <text>: returns a Math Bold Script
 """
 
BOX_HANDLER = DisableAbleCommandHandler("box", box, pass_args=True)
 
dispatcher.add_handler(BOX_HANDLER)
 
__mod_name__ = "Cool Text 🆒"
__command_list__ = ["box"]
__handlers__ = [BOX_HANDLER]
