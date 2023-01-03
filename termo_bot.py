import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp, User
from config import token
import sqlite3
import datetime as dt

banco = sqlite3.connect('database.db', check_same_thread=False)
c = banco.cursor()

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

#### FUNÇÕES ####

def verificar_se_existe_usuario(User):
    userid = User.id
    c.execute(f"SELECT * FROM usuarios WHERE id = '{userid}'")
    usuarios = c.fetchall()
    if usuarios:
        return True
    else:
        return False

def inserir_usuario(User):
    if verificar_se_existe_usuario(User):
        return False
    else:
        print(f"INSERT INTO usuarios (id, nome, data_registro) VALUES ({User.id}, {User.first_name}, '{ dt.datetime.now() }')")
        c.execute(f"INSERT INTO usuarios (id, nome, data_registro) VALUES ('{User.id}', '{User.first_name}', '{ dt.datetime.now() }')")
        banco.commit()
        return True


def start_bot():

    pass

### HANDLER PARA START ###
@bot.message_handler(commands=['start'])
def start(msg):
    User = msg.chat
    inserir_usuario(User)
    userid = User.id
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