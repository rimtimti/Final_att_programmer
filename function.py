from models import Animal
from datetime import datetime
import re


def menu(info: str, commands: str) -> str:
    '''
    Выводит на экран меню, возвращает выбранную команду
    '''
    choice = ''
    while choice not in commands:
        print(info)
        choice = input('Введите команду: ')
        if choice in commands:
            return choice
        else:
            print('Такой команды нет, попробуйте еще раз...')


def check_text(txt: str) -> str:
    '''
    Принимает ключевое слово. Проверяет введенную строку на присутствие только букв.
    '''
    text = ''
    text = input(f'Введите {txt}: ')
    while text.isalpha():
        return text
    else:
        print('Данные должны содержать только буквы!')
        return check_text(txt)


def check_date() -> str:
    '''
    Проверяет введенную строку на корректную дату.
    '''
    birthdate = input('Введите дату в формате dd.mm.yyyy: ')
    while re.match(r'\d\d\.\d\d\.\d\d\d\d$', birthdate):
        try:
            if datetime.strptime(birthdate, "%d.%m.%Y"):
                if datetime.strptime(birthdate, "%d.%m.%Y") < datetime.now():
                    return str(datetime.strptime(birthdate, "%d.%m.%Y").date())
                    break
                else:
                    print('Дата еще не наступила...')
                    return check_date()
        except:
            print('Дата введена неверно.')
            return check_date()
    else:
        print('Дата введена неверно.')
        return check_date()


def create_animal() -> Animal:
    '''
    Создает животное
    '''
    name = check_text('имя')
    birthdate = check_date()
    commands = []
    command = ''
    choice = 0
    while choice != '2':
        choice = menu('\n1 - Ввести комманду, которую животное умеет выполнять:\n2 - продолжить', ['1', '2'])
        if choice == '1':
            command = check_text('команду, которую животное умеет выполнять')
            commands.append(command)
    return Animal(name, birthdate, commands)


def check_int(input_string: str, number: int) -> int:
    '''
    Просит у пользователя ввести целое положительное число от 0 до number и проверяет его
    '''
    try:
        number_int = int(input(input_string))
        if number_int < 0 or number_int > number:
            print('Вы ввели неверное число.')
            return check_int(input_string, number)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return check_int(input_string, number)


def show_base(animal_list: list):
    '''
    Выводит на экран список животных
    '''
    print('\n')
    i = 1
    for animal in animal_list:
        print(f'{i} - {view_animal(animal)}')
        i += 1


def view_animal(animal: Animal) -> dict:
    '''
    Создает красивый словарь из данных о животном
    '''
    data_dict = {'Категория': animal.category,
                 'Тип животного': animal.animal_type,
                 'Имя': animal.name,
                 'Дата рождения': animal.birthdate,
                 'Команды': animal.commands}
    return data_dict


def write_to_file(animal_list: list, filename: str):
    '''
    Записывает данные в файл
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        for animal in animal_list:
            file.write(animal.__str__() + '\n')


def read_file(filename: str) -> list:
    '''
    Считывает данные из файла
    '''
    animal_list = []
    with open(filename, 'r', encoding='utf-8') as file:
        for f in file:
            if f != [' ', '', '\n']:
                array = f.strip().split(';')
                animal = Animal(array[2], array[3], array[4])
                animal.category = array[0]
                animal.animal_type = array[1]
                animal_list.append(animal)
    return animal_list
