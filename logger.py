import telebot
from datetime import datetime as dt

def log(message):
    time = dt.now().strftime("'%d.%m.%Y %H:%M'")
    file = open('db.csv', 'a', encoding='utf-8-sig')
    file. write(f'{time}, user_name: {message.from_user.first_name}, user_id: {message.from_user.id}, user_text: {message.text} \n')
    file.close
    