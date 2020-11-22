import csv
import datetime
import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types

url = "https://valuta.kg/"


def get_html(url):
    response = requests.get(url)
    return response.text


def write_csv(data):
    with open('banks_exchange.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((
            data['bank'],
            data["Dollar buy"],
            data['Dollar sell'],
            data['Euro buy'],
            data['Euro sell'],
            data['Rub buy'],
            data['Rub sell'],
            data['KZT buy'],
            data['KZT sell'],
        ))

def get_page_info(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_bank = soup.find_all("div", class_='td-member__info')
    all_purchase = soup.find_all('div', class_='td-rate__wrp')
    all_exchange = []
    for i in all_purchase:
        a = i.text
        a = a.strip()
        all_exchange.append(a)
    try:
        for bank in all_bank:
            bank = bank.find('h4').find('a').text
                
            dollar_buy = all_exchange[0]
            dollar_sell = all_exchange[1]
            euro_buy = all_exchange[2]
            euro_sell = all_exchange[3]
            rub_buy = all_exchange[4]
            rub_sell = all_exchange[5]
            tenge_buy = all_exchange[6]
            tenge_sell = all_exchange[7]
        
            bank_exchange ={
                'bank': bank,
                "Dollar buy" : dollar_buy,
                "Dollar sell" : dollar_sell,
                "Euro buy" : euro_buy,
                "Euro sell" : euro_sell,
                "Rub buy" : rub_buy,
                "Rub sell" : rub_sell,
                "KZT buy" : tenge_buy,
                "KZT sell" : tenge_sell,
            }
            del(all_exchange[:8])
            write_csv(bank_exchange)
    except:
        pass
        
    return

def parse_valutakg():
    html_text = get_html(url)
    all_bank = get_page_info(html_text)





if __name__ == '__main__':
    parse_valutakg()