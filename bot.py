import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from config import token

bot = telebot.TeleBot(token)

url_termo = 'https://term.ooo/'
markup_termo = InlineKeyboardMarkup(
    keyboard=[
        [
            InlineKeyboardButton(
                text="Abrir TERMO 🔠",
                web_app =  WebAppInfo(url=url_termo),
            )
        ]
    ]
)

######### HANDLER PARA QUALQUER MENSAGEM ###############
@bot.message_handler(func=lambda m: True)
def pagina_inicial(msg):
    userid = msg.chat.id
    username = msg.chat.first_name
    
    bot.send_message(userid, f'<strong>Olá, {username}!</strong> \n \n Clique no botão abaixo para abrir o TermOoo de hoje!', parse_mode='HTML', reply_markup=markup_termo)


bot.infinity_polling()