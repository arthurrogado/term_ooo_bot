import sqlite3
import datetime

banco = sqlite3.connect('database.db', check_same_thread=False)
c = banco.cursor()

def verificar_se_existe_usuario(userid):
    print('iniciando teste')
    c.execute(f"SELECT * FROM usuarios WHERE id = '{userid}'")
    usuarios = c.fetchall()
    if usuarios:
        return True
    else:
        return False

if verificar_se_existe_usuario(860446631):
    print('Sim, existe')
else:
    print('Não existe!!')

print(datetime.datetime.today())