from bs4 import BeautifulSoup
from telebot import TeleBot, types 
import requests
import csv
import json
import min_max_exchange


TOKEN = "1452583001:AAG5Teqf1RLWjZNjTa5tRDn-aIUlyS9Tv6w"
url = "https://valuta.kg/"
HEADERS = {
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'
}


bot = TeleBot(TOKEN)
main_keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton("USD", callback_data="America")
btn2 = types.InlineKeyboardButton("EUR", callback_data="Europe")
btn3 = types.InlineKeyboardButton("RUB", callback_data="Russia")
btn4 = types.InlineKeyboardButton("KZT", callback_data="Kazakhstan")
main_keyboard.add(btn1, btn2, btn3, btn4)



@bot.message_handler(commands = ['Start'])
def start(message):
    chat_id = message.chat.id
    bot.send_sticker(chat_id, 'CAACAgIAAxkBAAMNX7J9SSbwGpXGXARpTElJjtvDHcsAAhAAA8NWAx52cBQqdOh36x4E')
    bot.send_message(chat_id, "Пробиваем курсы валют!", reply_markup=main_keyboard)
    
    income_expenses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)


    a = types.KeyboardButton("Покупка")
    b = types.KeyboardButton("Продажа")
    income_expenses_keyboard.add(a, b)



@bot.callback_query_handler(func = lambda x: True)
def callback(x):

    chat_id = x.message.chat.id
    income_expenses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if x.data == 'America' :

        a = types.KeyboardButton("Покупка")
        b = types.KeyboardButton("Продажа")
        income_expenses_keyboard.add(a, b)
        
        msg = bot.send_message (chat_id, 'Выберите категорию',reply_markup = income_expenses_keyboard)
        bot.register_next_step_handler(msg, USD_CON)


    elif x.data == 'Europe' :

        a = types.KeyboardButton("Покупка")
        b = types.KeyboardButton("Продажа")
        income_expenses_keyboard.add(a, b)
        
        msg = bot.send_message (chat_id, 'Выберите категорию',reply_markup = income_expenses_keyboard)
        bot.register_next_step_handler(msg, EURO_CON)

    elif x.data == 'Russia' :

        a = types.KeyboardButton("Покупка")
        b = types.KeyboardButton("Продажа")
        income_expenses_keyboard.add(a, b)
        
        msg = bot.send_message (chat_id, 'Выберите категорию',reply_markup = income_expenses_keyboard)
        bot.register_next_step_handler(msg, RUB_CON)

    elif x.data == 'Kazakhstan' :

        a = types.KeyboardButton("Покупка")
        b = types.KeyboardButton("Продажа")
        income_expenses_keyboard.add(a, b)
        
        msg = bot.send_message (chat_id, 'Выберите категорию',reply_markup = income_expenses_keyboard)
        bot.register_next_step_handler(msg, KZT_CON)

#==================================================================

def USD_CON(message):

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Покупка' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, USD_MAX_RES)

    elif message.text == 'Продажа' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, USD_MIN_RES)

#==================================================================

def EURO_CON(message):

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Покупка' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, EURO_MAX_RES)

    elif message.text == 'Продажа' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, EURO_MIN_RES)

#==================================================================

def RUB_CON(message):

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Покупка' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, RUB_MAX_RES)

    elif message.text == 'Продажа' :


        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, RUB_MIN_RES)

#==================================================================

def KZT_CON(message):

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Покупка' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, KZT_MAX_RES)

    elif message.text == 'Продажа' :

        a = types.KeyboardButton ('Сохранить')
        b = types.KeyboardButton ('Лучшая цена')
        keyboard.add(a, b)
        msg = bot.send_message(chat_id, 'Выберите категорию',reply_markup=keyboard)
        bot.register_next_step_handler(msg, KZT_MIN_RES)



#==================================================================

def USD_MIN_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.min_exchange('Dollar sell'))
        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)



def USD_MAX_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.max_exchange('Dollar buy'))

        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        bot.send_message(chat_id, min_max_exchange.min_exchange('Dollar sell'))
        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)


#==================================================================

def EURO_MIN_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.min_exchange('Euro sell'))


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)


def EURO_MAX_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.max_exchange('Euro buy'))


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

#==================================================================

def RUB_MIN_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.min_exchange('Rub sell'))

   
        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')

  
        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)


def RUB_MAX_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.max_exchange('Rub buy'))

   
        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

#==================================================================

def KZT_MIN_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)

    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.min_exchange('KZT sell'))


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

def KZT_MAX_RES (message) :

    chat_id = message.chat.id
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    
    if message.text == 'Лучшая цена' :
        bot.send_message(chat_id, min_max_exchange.max_exchange('KZT buy'))


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)

    elif message.text == 'Сохранить' :
        with open('banks.json', 'r') as file:
            bot.send_document(chat_id, file, 'banks.json')


        quit_btn = types.KeyboardButton('Выйти')
        keyboard.add(quit_btn)
        msg = bot.send_message(chat_id, 'Нажите чтобы выйти', reply_markup = keyboard)
        bot.register_next_step_handler(msg, quit_chat)


def quit_chat (message) :

    chat_id = message.chat.id
    
    if message.text == 'Выйти' :
        bot.send_message(chat_id, 'Пока,  приходи еще!')
        bot.send_sticker(chat_id, 'CAACAgIAAxkBAAJdeV-31TNg3vJzMRBZJririMgIBWktAAIcAAPDVgMeBpkYYge3RLceBA')



bot.polling()