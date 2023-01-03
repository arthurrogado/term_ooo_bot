import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo, MenuButtonWebApp, User
from config import token
import sqlite3
import datetime

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
    print('iniciando teste')
    c.execute(f"SELECT * FROM usuarios WHERE id = '{userid}'")
    usuarios = c.fetchall()
    if usuarios:
        return True
    else:
        return False

def inserir_usuario(User):
    userid = User.id
    if verificar_se_existe_usuario(userid):
        c.execute(f"INSERT INTO usuario (id, nome, ultimo_jogo) VALUES ({userid}, {User.first_name}, {datetime.datetime.now('America/Sao_Paulo')})")
        banco.commit()
        return True
    else:
        return False

def atualizar_ultimo_jogo(userid):
    if verificar_se_existe_usuario(userid):
        if c.execute(f'UPDATE usuarios WHERE id = {userid} SET ultimo_jogo = {datetime.datetime.now("America/Sao_Paulo")}'):
            banco.commit()
            return True
    return False


def start_bot():
    pass

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