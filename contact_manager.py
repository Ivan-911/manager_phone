import os

# from lection7 import task1
from task1 import *


def read_phone(file_out):
    """Читает нужный файл"""
    with open(file_out, 'r') as f:
        buff_data = {}
        for i, sentence in enumerate(f):
            buff_data[i] = sentence
    return buff_data


def number_row(temp_sentence, file_in):
    """Записывает значение"""
    with open(file_in, 'a') as f:
        f.write('\n' + temp_sentence.rstrip('\n'))
    return read_phone(file_in)


if __name__ == '__main__':
    str_in = ["Укажите номер строки для копирования в ваш список контактов.",
              "Укажите номер строки чтоб поделится вашим контактом."]
    number_menu = 0
    while 1:
        file = ['phone.txt', 'my_phone.txt']
        data = {}
        data_out = {}
        if number_menu == 0:
            print("""Добро пожаловать в менеджер контактов!!
                Что я умею:-)
                1) Добавлю контакт в вашу телефонную книгу.
                2) Поделюсь вашим контактом.
                3)Изменю режим на телефонный справочник.
                4)Выход """)
            print("Пожалуйста введите номер команды")
            user_answer = input('Номер команды: ')
            if user_answer.isdigit() and 0 < int(user_answer) < 5:
                if user_answer == '1':
                    data = read_phone(file[0])
                    data['file_index'] = 0
                    number_menu = 1
                if user_answer == '2':
                    data = read_phone(file[1])
                    data['file_index'] = 1
                    number_menu = 1
                if user_answer == '3':
                    main()
                if user_answer == '4':
                    print("Работа завершена! До свидания ;-)")
                    break

        while number_menu == 1:
            for key, values in data.items():
                if key != 'file_index':
                    print(key, '-номер строки. Строка: ', values)
            print(str_in[data['file_index']],
                  "Или дважды Enter для выхода в главное меню")
            user_answer = input("Введите команду: ")
            if not user_answer:
                number_menu = 0
                continue
            if user_answer.isdigit() and data.get(int(user_answer), False):
                data_out = number_row(data[int(user_answer)], file[data['file_index'] - 1])
                print("Строка", data[int(user_answer)], "перенесена в список контактов!")
                for sentence in data_out.values():
                    print(sentence)
                print('-*-' * 15)
            else:
                print("Упс что-то пошло не так! :-(")
                print("Проверьте верно ли указан номер строки и повторите попытку.")

