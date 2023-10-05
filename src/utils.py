import json
import datetime

def load_operations():
    # Функция загружает список банковских операций из файла JSON
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


def get_filtered_executed(operations):
    '''Функция получает словарь с данными по выполненным банковским операциям.
    #     Пример вывода для одной операции:
    #     14.10.2018 Перевод организации
    #     7000 79** **** 6361 -> Счет **9638
    #     82771.72 руб.'''
    return [x for x in operations if "state" in x and x["state"] == "EXECUTED"]


def get_last_operations(operations):
    # Функция выбирает пять последних выполненных операций и сортирует их по дате
    operations = sorted(operations, key=lambda x: x['date'], reverse=True)[:5]
    return operations


def datetime_operations(data):
    # Функция форматирует дату в формат: 14.10.2018
    for i in data:
        date = datetime.datetime.strptime(i['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        i["date"] = date



def number_card_cod(data):
    # Функция зашифровывает номер карты в формат: Visa Platinum 7000 79** **** 6361)
    for i in data:
        if 'from' in i:
            card = i["from"].split()
            card_number = card.pop()
            sicret_number = f'{card_number[:4]} {card_number[5:7]}** *** {card_number[-4:]}'
            i["from"] = " ".join(card) + " " + sicret_number
        else:
            i['from'] = 'None'


def number_check_cod(data):
    # Функция зашифровывает номер счета в формат: Счет **9638
    for i in data:
        check = i["to"].split()
        check_number = check.pop()
        sicret_number = f'**{check_number[-4:]}'
        i["to"] = " ".join(check) + " " + sicret_number

