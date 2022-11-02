class Person:
    def __init__(self):
        self.__name = None
        self.__X_coord = 0
        self.__Y_coord = 0
        self.__health = 100

    @property
    def y(self):
        print ('called getter <y>')
        return self.__Y_coord

    @property
    def x(self):
        print('called getter <x>')
        return self.__X_coord

    @property
    def health(self):
        print('called getter <health>')
        return self.__health

    @property
    def name(self):
        print('called getter <name>')
        return self.__name

    @name.setter
    def name(self, name):
        print('called setter <name>')
        self.__name = name

    def move(self, x_input, y_input): ## методы не требуют обращения к @.setter
        self.__X_coord += x_input
        self.__Y_coord += y_input

    def display_info(self):
        print(f'{self.__name} находится в точке ({self.__X_coord}, {self.__Y_coord}), его здоровье {self.__health} ')


def main():
    person = Person()
    person.name = 'Серега'
    person.display_info()
    x_input = int(input(f' Введите, на сколько передвинется {person.name} по оси Х: '))
    y_input = int(input(f' Введите, на сколько передвинется {person.name} по оси Y: '))
    person.move(x_input, y_input)
    person.display_info()


main()


