from telegram.ext import Updater,Filters,CallbackContext
from telegram import Update
from googletrans import Translator
tranlator = Translator()

def start(update:Update,context:CallbackContext):
    name = update.message.from_user.first_name
    update.message.reply_text(f'Assalomu alaylum {name}\n Botimizga hush kelibsiz.Bu speak Enlish boti')


def tarjimon(update:Update,context:CallbackContext):
    m_text = update.message.text
    lang = tranlator.detect(m_text).lang
    print(lang)
    if lang == 'en':
        update.message.reply_text(tranlator.translate(m_text,dest='uz').text)
    else:
        update.message.reply_text(tranlator.translate(m_text,dest='en').text)