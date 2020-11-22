import requests
from bs4 import BeautifulSoup
import json


url = "https://valuta.kg/"

def get_html(url):
    response = requests.get(url)
    return response.text

def write_json(banks):
    with open ('banks.json', 'w+', encoding='utf-8') as file :
        for a in banks:
            json.dump(a, file, ensure_ascii=False)
            file.write('\n')



def all_banks(html):
    global all_banks
    soup = BeautifulSoup(html, 'html.parser')
    all_bank = soup.find_all("div", class_='td-member__info')
    all_purchase = soup.find_all('div', class_='td-rate__wrp')
    all_exchange = []
    all_banks = []
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
            all_banks.append(bank_exchange)

    except:
        pass
    return all_banks


def min_exchange(exchange):
    all_exchange = []

    for a in all_exchange_banks:
        all_exchange.append(a[exchange])

    bank = ""

    min_ex = []

    
    for a in all_exchange:
        try:
            a = float(a)
            min_ex.append(a)
        except:
            continue

    min_exchange = min(min_ex)
    

    steps = 0
    b = 0
    for a in all_exchange_banks:
        for bank in a.values():
            try:
                bank = float(bank)
                if bank == min_exchange:

                    b += 1
                    break
                
                elif steps == 9:
                    break
                
                else:
                    steps += 1
                    continue
            except:
                continue
            
        if b == 0:
            steps = 0
            continue     
        elif b == 1:
            bank = a['bank']
            break

    message = f"Самый выгодный курс  {min_exchange}  в  {bank}  "
    return message

def max_exchange(exchange):
    all_exchange = []

    for a in all_exchange_banks:
        all_exchange.append(a[exchange])

    bank = ""

    max_ex = []

    
    for a in all_exchange:
        try:
            a = float(a)
            max_ex.append(a)
        except:
            continue

    max_exchange = max(max_ex)
    
    steps = 0
    b = 0
    for a in all_exchange_banks:
        for bank in a.values():
            try:
                bank = float(bank)
                if bank == max_exchange:
                    b += 1
                    break
                
                elif steps == 9:
                    break
                
                else:
                    steps += 1
                    continue
            except:
                continue
            
        if b == 0:
            steps = 0
            continue     
        elif b == 1:
            bank = a['bank']
            break

    message = f"Самый выгодный курс  {max_exchange}  в  {bank}  "
    return message


html_text = get_html(url)
all_exchange_banks = all_banks(html_text)
json = write_json(all_exchange_banks)


