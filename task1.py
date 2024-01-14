"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
Программа должна выводить данные
Программа должна сохранять данные в текстовом файле
Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
Использование функций. Ваша программа не должна быть линейной"""

import os


def input_data(data):
    while True:
        user_input = input('введите номер телефона: ')
        if not user_input or not user_input.isdigit():
            return data
        if user_input in data:
            print('Такой номер уже есть!')
        else:
            temp = input("ФИО через пробел: ").split()
            if len(temp) != 3:
                print('Ошибка')
            else:
                data[user_input] = temp
                with open('phone.txt', 'a') as f:
                    print(f"{user_input}\t{temp[0]}\t{temp[1]}\t{temp[2]}", file=f)
                return data


def show_data(data):
    for key, value in data.items():
        print(key, *value)


def search_data(data):
    user_input = input("Поиск 1: номер телефона или 2: иное")
    if user_input not in {'1', '2'}:
        return
    if user_input == '1':
        phone = input("введите номер телефона: ")
        print(data.get(phone, 'Нет номера'))
        return
    other = input("Имя или Фамилия или Отчество")
    if ' ' in other or not other:
        print('Ошибка')
        return
    for key, values in data.items():
        for value in values:
            if other in value:
                print(key, *values)
                break


def main():
    if os.path.exists('phone.txt'):
        with open('phone.txt', 'r+') as file:
            data = {}
            for sentence in file:
                phone, second_name, first_name, third_name = sentence.split()
                data[phone] = [second_name, first_name, third_name]
    else:
        with open('phone.txt', 'w') as f:
            data = {}

    print("Добро пожаловать в телефонный справочник")
    while True:
        while True:
            user_input = input("""1: ввести новые данные \n2:просмотреть данные \n3:поиск \n4:выход\n""")
            if user_input not in {'1', '2', '3', '4'}:
                print('Неверное значение!')
            else:
                break
        if user_input == '1':
            data = input_data(data)
        elif user_input == '2':
            show_data(data)
        elif user_input == '3':
            search_data(data)
        else:
            print('До свидания!!')
            break


if __name__ == '__main__':
    main()
