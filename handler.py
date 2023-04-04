from telegram.ext import Updater,Filters,CallbackContext
from telegram import Update
from googletrans import Translator
from api import query

tranlator = Translator()

def start(update:Update,context:CallbackContext):
    name = update.message.from_user.first_name
    update.message.reply_text(f'Assalomu alaylum {name}\n Botimizga hush kelibsiz.Bu speak Enlish boti')


def tarjimon(update:Update,context:CallbackContext):
    m_text = update.message.text
    lang = tranlator.detect(m_text).lang
    
    print(lang)
    if len(m_text.split()) >= 2:
        if lang == 'en':
            update.message.reply_text(tranlator.translate(m_text,dest='uz').text)
        else:
            update.message.reply_text(tranlator.translate(m_text,dest='en').text)
    else:
        if lang == 'en':
            word_id = m_text
            word = query(word_id)
        else:
            word_id = tranlator.translate(m_text,dest='en').text
            word = query(word_id)
        if word:
            update.message.reply_text(f"Word: {word_id} \nDefinitions: \n{word['definitions']}")
        else:
            update.message.reply_text('Bunday so\'z topilmadi')