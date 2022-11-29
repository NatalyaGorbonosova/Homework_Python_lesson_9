import telebot
import json
import re
import rational as rat
import requests
import logger as lg

API_URL = 'https://7012.deeppavlov.ai/model'

API_TOKEN = '5754862285:AAF1AEqLUxqmn1w1tQfEVRNg3Rt6q1T9pVM'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    lg.log(message)
    mess = f'Привет, {message.from_user.first_name}! \n Готов к работе!'
    bot.send_message(message.chat.id, mess)
    

@bot.message_handler(commands=['calc'])
def calc_message(message):
    lg.log(message)
    eq = message.text.split()[1:]   
    if 'j' in eq[0]: 
        bot.send_message(message.chat.id, eval(eq[0]))
    else: 
        bot.send_message(message.chat.id, rat.rational(eq[0]))

@bot.message_handler(commands=['wiki'])
def wiki_question(message):
    lg.log(message)
    question = message.text.split()[1:]
    quest = ' '.join(question)
    data = {'question_raw': [quest]}
    try:
        res = requests.post(API_URL, json=data, verify=False).json()
        bot.send_message(message.chat.id, res)
    except:
        bot.send_message(message.chat.id, 'Ничего не найдено')

bot.polling()