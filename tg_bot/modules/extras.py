import random
import re

from random import randint

from telegram import Message, Update, Bot, User, MessageEntity
from telegram.ext import MessageHandler, CallbackContext, Filters, run_async

from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

EYES = [
    ['⌐■', '■'],
    [' ͠°', ' °'],
    ['⇀', '↼'],
    ['´• ', ' •`'],
    ['´', '`'],
    ['`', '´'],
    ['ó', 'ò'],
    ['ò', 'ó'],
    ['⸌', '⸍'],
    ['>', '<'],
    ['Ƹ̵̡', 'Ʒ'],
    ['ᗒ', 'ᗕ'],
    ['⟃', '⟄'],
    ['⪧', '⪦'],
    ['⪦', '⪧'],
    ['⪩', '⪨'],
    ['⪨', '⪩'],
    ['⪰', '⪯'],
    ['⫑', '⫒'],
    ['⨴', '⨵'],
    ['⩿', '⪀'],
    ['⩾', '⩽'],
    ['⩺', '⩹'],
    ['⩹', '⩺'],
    ['◥▶', '◀◤'],
    ['◍', '◎'],
    ['/͠-', '┐͡-\\'],
    ['⌣', '⌣”'],
    [' ͡⎚', ' ͡⎚'],
    ['≋'],
    ['૦ઁ'],
    ['  ͯ'],
    ['  ͌'],
    ['ළ'],
    ['◉'],
    ['☉'],
    ['・'],
    ['▰'],
    ['ᵔ'],
    [' ﾟ'],
    ['□'],
    ['☼'],
    ['*'],
    ['`'],
    ['⚆'],
    ['⊜'],
    ['>'],
    ['❍'],
    ['￣'],
    ['─'],
    ['✿'],
    ['•'],
    ['T'],
    ['^'],
    ['ⱺ'],
    ['@'],
    ['ȍ'],
    ['  '],
    ['  '],
    ['x'],
    ['-'],
    ['$'],
    ['Ȍ'],
    ['ʘ'],
    ['Ꝋ'],
    [''],
    ['⸟'],
    ['๏'],
    ['ⴲ'],
    ['◕'],
    ['◔'],
    ['✧'],
    ['■'],
    ['♥'],
    [' ͡°'],
    ['¬'],
    [' º '],
    ['⨶'],
    ['⨱'],
    ['⏓'],
    ['⏒'],
    ['⍜'],
    ['⍤'],
    ['ᚖ'],
    ['ᴗ'],
    ['ಠ'],
    ['σ'],
    ['☯']
]

MOUTHS = [
    ['v'],
    ['ᴥ'],
    ['ᗝ'],
    ['Ѡ'],
    ['ᗜ'],
    ['Ꮂ'],
    ['ᨓ'],
    ['ᨎ'],
    ['ヮ'],
    ['╭͜ʖ╮'],
    [' ͟ل͜'],
    [' ͜ʖ'],
    [' ͟ʖ'],
    [' ʖ̯'],
    ['ω'],
    [' ³'],
    [' ε '],
    ['﹏'],
    ['□'],
    ['ل͜'],
    ['‿'],
    ['╭╮'],
    ['‿‿'],
    ['▾'],
    ['‸'],
    ['Д'],
    ['∀'],
    ['!'],
    ['人'],
    ['.'],
    ['ロ'],
    ['_'],
    ['෴'],
    ['ѽ'],
    ['ഌ'],
    ['⏠'],
    ['⏏'],
    ['⍊'],
    ['⍘'],
    ['ツ'],
    ['益'],
    ['╭∩╮'],
    ['Ĺ̯'],
    ['◡'],
    [' ͜つ']
]

EARS = [
    ['q', 'p'],
    ['ʢ', 'ʡ'],
    ['⸮', '?'],
    ['ʕ', 'ʔ'],
    ['ᖗ', 'ᖘ'],
    ['ᕦ', 'ᕥ'],
    ['ᕦ(', ')ᕥ'],
    ['ᕙ(', ')ᕗ'],
    ['ᘳ', 'ᘰ'],
    ['ᕮ', 'ᕭ'],
    ['ᕳ', 'ᕲ'],
    ['(', ')'],
    ['[', ']'],
    ['¯\\_', '_/¯'],
    ['୧', '୨'],
    ['୨', '୧'],
    ['⤜(', ')⤏'],
    ['☞', '☞'],
    ['ᑫ', 'ᑷ'],
    ['ᑴ', 'ᑷ'],
    ['ヽ(', ')ﾉ'],
    ['\\(', ')/'],
    ['乁(', ')ㄏ'],
    ['└[', ']┘'],
    ['(づ', ')づ'],
    ['(ง', ')ง'],
    ['⎝', '⎠'],
    ['ლ(', 'ლ)'],
    ['ᕕ(', ')ᕗ'],
    ['(∩', ')⊃━☆ﾟ.*'],
]

TOSS = (
    "Heads",
    "Tails",
)

@run_async
def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))

@run_async
def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(TOSS))

@run_async
def shrug(update: Update, context: CallbackContext):
    
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("¯\\_(ツ)_/¯")

@run_async
def bluetext(update: Update, context: CallbackContext):
    
    reply_text = update.effective_message.reply_to_message.reply_text if update.effective_message.reply_to_message else update.effective_message.reply_text
    reply_text("/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS")

@run_async
def rlg(update: Update, context: CallbackContext):
    
    eyes = random.choice(EYES)
    mouth = random.choice(MOUTHS)
    ears = random.choice(EARS)
    
    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)

@run_async
def decide(update: Update, context: CallbackContext):
    r = randint(1, 100)
    if r <= 65:
        update.message.reply_text("Yes.")
    elif r <= 90:
        update.message.reply_text("NoU.")
    else:
        update.message.reply_text("Maybe.")

@run_async
def table(update: Update, context: CallbackContext):
    r = randint(1, 100)
    if r <= 50:
        update.message.reply_text("(╯°□°）╯彡 ┻━┻")
    else:
        update.message.reply_text("Go do some work instead of flippin tables you helpless fagit.")

__help__ = """
 - /shrug : get shrug XD.
 - /table : get flip/unflip :v.
 - /decide : Randomly answers yes/no/maybe
 - /toss : Tosses A coin
 - /abuse : Abuses the cunt
 - /bluetext : check urself :V
 - /roll : Roll a dice.
 - /rlg : Join ears,nose,mouth and create an emo ;-;
"""

SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug)
TABLE_HANDLER = DisableAbleCommandHandler("table", table)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg)

dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(RLG_HANDLER)

__mod_name__ = "Extras"
__command_list__ = ["shrug", "table", "decide", "toss", "bluetext", "roll", "rlg"]
__handlers__ = [SHRUG_HANDLER, TABLE_HANDLER, DECIDE_HANDLER, TOSS_HANDLER, BLUETEXT_HANDLER, ROLL_HANDLER, RLG_HANDLER]
