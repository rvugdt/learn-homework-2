"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

import csv

def main():
    data = [
        {'name':'Иван', 'age':'21', 'job':'Менеджер'},
        {'name':'Елена', 'age':'22', 'job':'Библиотекарь'},
        {'name':'Сергей', 'age':'25', 'job':'Инженер'},
        {'name':'Дарья', 'age':'28', 'job':'Учитель'},
        {'name':'Дмитрий', 'age':'29', 'job':'Продавец'},
        {'name':'Наталья', 'age':'26', 'job':'Домохозяйка'}
    ]

    keys = data[0].keys()

    with open('data.csv', 'w') as output_file:
        wrtr = csv.DictWriter(output_file, keys, delimiter='\t')
        wrtr.writeheader()
        wrtr.writerows(data)

if __name__ == "__main__":
    main()
