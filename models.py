class Animal:
    def __init__(self, name, birthdate, commands):
        self.name = name
        self.birthdate = birthdate
        self.commands = commands

    def __str__(self):
        return f'{self.name};{self.birthdate};{self.commands}'


class Pet(Animal):
    category = 'Домашнее животное'
    animal_type = ''
    
    def __str__(self):
        return f'{self.category};'\
               f'{self.animal_type};'\
               f'{super().__str__()}'


class PackAnimal(Animal):
    category = 'Вьючное  животное'
    animal_type = ''
    
    def __str__(self):
        return f'{self.category};'\
               f'{self.animal_type};'\
               f'{super().__str__()}'

class Dog(Pet):
    animal_type = 'Собака'

    def __str__(self):
        return super().__str__()
    

class Cat(Pet):
    animal_type = 'Кошка'

    def __str__(self):
        return super().__str__()


class Hamster(Pet):
    animal_type = 'Хомяк'

    def __str__(self):
        return super().__str__()


class Horse(PackAnimal):
    animal_type = 'Лошадь'

    def __str__(self):
        return super().__str__()


class Camel(PackAnimal):
    animal_type = 'Верблюд'

    def __str__(self):
        return super().__str__()


class Donkey(PackAnimal):
    animal_type = 'Осел'

    def __str__(self):
        return super().__str__()


class Counter():

    def __init__(self):
        self.value = 0

    def new_value(self):
        self.value += 1
        return self.value

    def __str__(self):
        return f'{self.value}'
