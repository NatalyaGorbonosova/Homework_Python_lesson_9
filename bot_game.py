import telebot
import re
import random
import logger as lg

def print_field(matrix):
    str = ''
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            str += matrix[i][j]
        str += '\n'
    return str

def bot_stroke(matrix):
    try:
        list_empty = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == ' - ': list_empty.append([i, j])
        stroke = random.choice(list_empty)
        return stroke
    except: bot.send_message(message.chat.id, 'Конец игры')

def check_win(matrix):
    check = 0
    for i in range(len(matrix)):
        if matrix[i] == [' x ', ' x ', ' x ']:
            check = 1
            break
        elif matrix[i] == [' 0 ', ' 0 ', ' 0 ']:
            check = 2
            break
    for j in range(len(matrix[0])):
        if matrix[0][j] == ' x ' and matrix[1][j] == ' x ' and matrix[2][j] == ' x ':
            check = 1
            break
        elif matrix[0][j] == ' 0 ' and matrix[1][j] == ' 0 ' and matrix[2][j] == ' 0 ':
            check = 2
            break
    if matrix[0][0] == matrix[1][1] == matrix[2][2] == ' x ' or matrix[0][2] == matrix[1][1] == matrix[2][0] == ' x ':
        check = 1
       
    elif matrix[0][0] == matrix[1][1] == matrix[2][2] == ' 0 ' or matrix[0][2] == matrix[1][1] == matrix[2][0] == ' 0 ':
        check = 2
    return check
def game_over(stroke_number, game_field):
    if stroke_number > 4:
            if check_win(game_field) == 1:
                return 'You win!!!'
            elif check_win(game_field) == 2:
                return 'Bot win'

def clear_game():
    game_field = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']] 
    return game_field

API_TOKEN = '5754862285:AAF1AEqLUxqmn1w1tQfEVRNg3Rt6q1T9pVM'

bot = telebot.TeleBot(API_TOKEN)
stroke_number = 0
game_field = [[' - ', ' - ', ' - '], [' - ', ' - ', ' - '], [' - ', ' - ', ' - ']] 

@bot.message_handler(commands=['start'])
def start_message(message):
    lg.log(message)
    bot.send_message(message.chat.id, "Готов к работе!")

@bot.message_handler(commands=['game'])
def calc_message(message):
    lg.log(message)
    str_game_field = print_field(game_field)
    bot.send_message(message.chat.id, 'Начинаем игру!!!')
    bot.send_message(message.chat.id, str_game_field)
    bot.send_message(message.chat.id, 'Сделай ход!!! Напиши номер строки и номер столбца через пробел, нумерация от 1 до 3')
    global stroke_number
    
    while stroke_number < 9:
        @bot.message_handler(content_types='text')
        def message_step(message):
            lg.log(message)
            global stroke_number
            global game_field
            str_mes = message.text
            list_step = re.split(r' ',str_mes)
            x = int(list_step[0])
            y = int(list_step[1])
            if game_field[x-1][y-1] == ' - ':
                game_field[x-1][y-1] = ' x '
                str_game_field = print_field(game_field)
                bot.send_message(message.chat.id, 'Вы походили')
                bot.send_message(message.chat.id, str_game_field)
            else: bot.send_message(message.chat.id, 'Эта ячейка уже заполнена, ход переходит противнику')
            stroke_number += 1
            result = game_over(stroke_number, game_field)
            if result == 'You win!!!' or result == 'Bot win':
                bot.send_message(message.chat.id, f' игра окончена {result} ')
                game_field = clear_game()
                return 
            stroke = bot_stroke(game_field)
            game_field[stroke[0]] [stroke[1]] = ' 0 '
            bot.send_message(message.chat.id,'Ход противника')
            str_game_field = print_field(game_field)
            bot.send_message(message.chat.id, str_game_field)
            stroke_number += 1
            result = game_over(stroke_number, game_field)
            if result == 'You win!!!' or result == 'Bot win':
                bot.send_message(message.chat.id, f' игра окончена {result} ')
                game_field = clear_game()
                return 
        
        break

bot.polling()