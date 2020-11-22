import requests
from bs4 import BeautifulSoup
from telebot import TeleBot , types
import csv 
import telegram_bot



bot = TeleBot('1452583001:AAG5Teqf1RLWjZNjTa5tRDn-aIUlyS9Tv6w')


main_keyboard = types.InlineKeyboardMarkup(row_width=2)
btn1 = types.InlineKeyboardButton("USD", callback_data="USD")
btn2 = types.InlineKeyboardButton("EUR", callback_data="EUR")
btn3 = types.InlineKeyboardButton('RUB', callback_data ='RUB')
btn4 = types.InlineKeyboardButton('KZT', callback_data ='KZT')

main_keyboard.add(btn1,btn2,btn3,btn4)


@bot.message_handler(commands=["start"])
def start(message):
    with open('banks_exchange.csv', 'w'):
        pass
    chat_id = message.chat.id
    bot.send_message(chat_id,"Приветствуем, выберите пожалуйста валюту",reply_markup=main_keyboard)
    telegram_bot.parse_valutakg()


def send_file(message):
    chat_id = message.chat.id
    if message.text == 'Сохранить':
        with open('banks_exchange.csv', 'r', encoding="UTF-8") as file:
            bot.send_document(chat_id, file, 'banks_exchange.csv')
            # bot.send_message(chat_id, "До встречи")
    else:
        bot.send_message(chat_id,)

    
        
@bot.callback_query_handler(lambda x:True)
def call_back(x):
    operation_keyboard =types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if x.data in ('USD','EUR','RUB','KZT'):
        btn1 = types.InlineKeyboardButton('Покупка',callback_data='Покупка')
        btn2 = types.InlineKeyboardButton('Продажа',callback_data='Продажа')
    operation_keyboard.add(btn1,btn2)
    msg = bot.send_message(x.message.chat.id,"Выберите нужную операцию", reply_markup=operation_keyboard)
    bot.register_next_step_handler(msg, operating)


def operating(message):
    choosing_keyboard =types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if message.text == "Покупка" or "Продажа":
        btn1 = types.InlineKeyboardButton('Сохранить')
        btn2 = types.InlineKeyboardButton('Вывести лучший курс')
    choosing_keyboard.add(btn1,btn2)
    msg = bot.send_message(message.chat.id,"Нажмите сохранить для получения данных по валютным курсам", reply_markup=choosing_keyboard)
    bot.register_next_step_handler(msg,send_file)



bot.polling()



