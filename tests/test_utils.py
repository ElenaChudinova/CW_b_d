from src.utils import get_filtered_executed, get_last_operations, number_check_cod, number_card_cod, datetime_operations

def test_get_filtered_executed(test_data):
    data = get_filtered_executed(test_data)
    assert data == [{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'}, {'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'}, {'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, {'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'}]


def test_get_last_operations(test_data):
    data = get_last_operations(test_data)
    assert [x["date"] for x in data] == ['2019-12-08T22:46:21.935582', '2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614', '2019-11-13T17:38:04.800051', '2019-11-05T12:04:13.781725']


def test_number_check_cod(test_data):
    number_check_cod(test_data)
    numbers = [x["to"] for x in test_data]
    print(numbers)
    assert numbers == ['Счет **5907', 'Счет **3655', 'Счет **2869', 'Счет **8125', 'Счет **8381']


def test_number_card_cod(test_data):
    number_card_cod(test_data)
    numbers = [x["from"] for x in test_data]
    print(numbers)
    assert numbers == ['None', 'Visa Classic 2842 78** *** 9012', 'Maestro 7810 46** *** 5568', 'Счет 3861 43** *** 9794', 'None']


def test_datetime_operations(test_data):
    datetime_operations(test_data)
    numbers = [x["date"] for x in test_data]
    print(numbers)
    assert numbers == ['08.12.2019', '07.12.2019', '19.11.2019', '13.11.2019', '05.11.2019']





