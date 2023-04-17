from function import menu, create_animal, check_int, read_file, write_to_file, show_base, view_animal
from models import Dog, Cat, Hamster, Horse, Camel, Donkey, Counter
from pathlib import Path


def run():
    '''
    Основная логика программы
    '''
    filename = Path('database_animals.csv')
    filename.touch(exist_ok=True)
    count = Counter()
    print('\nЭто программа "Реестр домашних животных".\n'
          'Вы можете вести учет животных: добавлять, удалять, просматривать и редактировать.\n')
    print('Выберите комманду.')
    while True:
        animal_list = read_file(filename)
        choice = menu(
            '\nОСНОВНОЕ МЕНЮ:\n1 - вывести всех животных\n2 - добавить животное\n3 - удалить животное\n4 - редактировать животное\n5 - выход', ['1', '2', '3', '4', '5'])
        if choice == '1':
            if animal_list == []:
                print(f'\nРеестр пока пуст...')
            else:
                show_base(animal_list)
        if choice == '3':
            if animal_list == []:
                print(f'\nРеестр пока пуст...')
            else:
                temp = check_int(
                    '\nВведите номер животного для удаления или 0 для возврата в основное меню: ', len(animal_list)) - 1
                if temp == -1:
                    continue
                else:
                    animal_list.pop(temp)
            write_to_file(animal_list, filename)
        if choice == '2':
            print(f'\nСоздаем животное...\n')
            animal = create_animal()
            type_animal = menu('\nВыберите тип животного: \n'
                               '1 - Собака\n'
                               '2 - Кошка\n'
                               '3 - Хомяк\n'
                               '4 - Лошадь\n'
                               '5 - Верблюд\n'
                               '6 - Осел', ['1', '2', '3', '4', '5', '6'])
            if type_animal == '1':
                new = Dog(animal.name, animal.birthdate, animal.commands)
            if type_animal == '2':
                new = Cat(animal.name, animal.birthdate, animal.commands)
            if type_animal == '3':
                new = Hamster(animal.name, animal.birthdate, animal.commands)
            if type_animal == '4':
                new = Horse(animal.name, animal.birthdate, animal.commands)
            if type_animal == '5':
                new = Camel(animal.name, animal.birthdate, animal.commands)
            if type_animal == '6':
                new = Donkey(animal.name, animal.birthdate, animal.commands)
            animal_list.append(new)
            count.new_value()
            write_to_file(animal_list, filename)
            print(f'Вы уже ввели: {count} животных')
        if choice == '4':
            if animal_list == []:
                print(f'\nРеестр пока пуст...')
            else:
                temp = check_int(
                    '\nВведите номер животного для редактирования или 0 для возврата в основное меню: ', len(animal_list)) - 1
                if temp == -1:
                    continue
                else:
                    print(view_animal(animal_list[temp]))
                    print(
                        f"\nВведите новое Имя, Дату рождения, Команды для этого животного.")
                    new = create_animal()
                    animal_list[temp].name = new.name
                    animal_list[temp].birthdate = new.birthdate
                    animal_list[temp].commands = new.commands
                write_to_file(animal_list, filename)
        if choice == '5':
            print(f'\nДо новых встреч... Данные записаны в файле database_animals.csv\n')
            break
