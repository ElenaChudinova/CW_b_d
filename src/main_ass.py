from utils import load_operations, datetime_operations, number_check_cod, get_filtered_executed, get_last_operations, number_card_cod


all_operations = load_operations()

operations_executed = get_filtered_executed(all_operations)
last_operations = get_last_operations(operations_executed)

date_operations = datetime_operations(all_operations)
number_card_cod = number_card_cod(all_operations)
number_check_cod = number_check_cod(all_operations)


for i in last_operations:
    print(date_operations.get("date"), i['description'],'\n', number_card_cod.get("from"), '->', number_check_cod.get("to"), '\n', i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
    print()









