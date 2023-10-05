from utils import load_operations, datetime_operations, number_check_cod, get_filtered_executed, get_last_operations, number_card_cod


all_operations = load_operations()

operations_executed = get_filtered_executed(all_operations)
last_operations = get_last_operations(operations_executed)

datetime_operations(last_operations)
number_card_cod(last_operations)
number_check_cod(last_operations)

for i in last_operations:
    print(i["date"], i['description'])
    print(i['from'], '->', i['to'])
    print(i['operationAmount']['amount'], i['operationAmount']['currency']['name'])
    print()



