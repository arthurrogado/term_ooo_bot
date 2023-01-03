import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp
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


### HANDLER PARA START ###
@bot.message_handler(commands=['start'])
def start(msg):
    userid = msg.chat.id
    menu = MenuButtonWebApp('web_app', text="Abrir TERMO 🔠" , web_app =  WebAppInfo(url=url_termo))
    bot.set_chat_menu_button(userid, menu)
    bot.send_message(userid, 'Clique no botão abaixo para abrir o app!')

######### HANDLER PARA QUALQUER MENSAGEM ###############
@bot.message_handler(func=lambda m: True)
def pagina_inicial(msg):
    userid = msg.chat.id
    username = msg.chat.first_name
    bot.send_message(userid, f'<strong>Olá, {username}!</strong> \n \n Clique no botão abaixo para abrir o TermOoo de hoje!', parse_mode='HTML', reply_markup=markup_termo)


bot.infinity_polling()