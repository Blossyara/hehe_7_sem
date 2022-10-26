# Работа на паре 2 (16.09.2022):
# Создать программу, которая печатает на экране анкету студента. Есть функция, которая принимает на вход имя, возраст,
# группу студента, а также три оценки по каким-либо предметам. Параметры по двум предметам из трех являются
# необязательными (то есть, могут задаваться по умолчанию). Есть функция расчета среднего, которая может
# принимать произвольное количество численных аргументов и возвращать среднее арифметическое по ним. Таким
# образом, функция, которая выводит на экран анкету студента выводит имя, фамилию, возраст и средний балл по
# всем предметам (то есть, вызывает внутри себя функцию расчета среднего)
import random


def create_rand_base(length):
    students_name = ['Саша', 'Ванес', 'Шамиль', 'Егор', 'Даня', 'Антоха', 'Сазик', 'Рафик', 'Миша Кнопочкин)',
                     'Лерибейби', 'Альбишка', 'Анастейшн', 'Мотя)', 'Димасик)', 'Мироша', 'Илья', 'Рустам4ик']
    students_group = ['К-15', 'К-17', 'К-25', 'К-27', 'К-35', 'К-45', 'Ц-21', 'Ц-22', 'К-31', 'К-32', 'К-41', 'К-42']
    students_base = []
    for i in range(length):
        students = [students_name[random.randint(0, len(students_name) - 1)], random.randint(17, 23),
                    students_group[random.randint(0, len(students_group) - 1)], random.randint(2, 5),
                    random.randint(2, 5), random.randint(2, 5)]
        students_base.append(students)
        i += 1
    return students_base


def average_calc(grades):
    summary = 0
    for grade in grades:
        summary += grade
    return summary / len(grades)


def show_base(students_base):
    print(
        '% -7s' % 'Номер студента',
        '% 10s' % 'Имя',
        '% 15s' % 'Возраст',
        '% 10s' % 'Группа',
        '% 15s' % 'Математика',
        '% 15s' % 'Физкультура',
        '% 15s' % 'Информатика',
    )
    for i in range(len(students_base)):
        print(
            '% -7s' % {i + 1},
            '% 20s' % {students_base[i][0]},
            '% 10s' % {students_base[i][1]},
            '% 13s' % {students_base[i][2]},
            '% 10s' % {students_base[i][3]},
            '% 15s' % {students_base[i][4]},
            '% 15s' % {students_base[i][5]},
        )


def insert_info(students_base):
    name = input('Введите имя студента: ')
    age = input('Введите возвраст студента: ')
    group = input('Введите группу студента: ')
    math_grade = int(input('Введите оценку студента по математике (обязательно): '))
    while math_grade > 5 or math_grade < 2:
        math_grade = int(input('Введите оценку студента по математике от 2 до 5 (обязательно): '))

    process = int(input('Хотите добавить оценку по физкультуре? \n 1. Да \n 2. Нет \n '))
    if process == 1:
        pe_grade = int(input('Введите оценку студента по физкультуре (опционально): '))
        while pe_grade > 5 or pe_grade < 2:
            pe_grade = int(input('Введите оценку студента по физкультуре от 2 до 5(опционально): '))
    else:
        pe_grade = None

    process = int(input('Хотите добавить оценку по информатике? \n 1. Да \n 2. Нет \n'))
    if process == 1:
        it_grade = int(input('Введите оценку студента по информатике (опционально): '))
        while it_grade > 5 or it_grade < 2:
            it_grade = int(input('Введите оценку студента по информатике от 2 до 5 (опционально): '))
    else:
        it_grade = None

    students_base.append([name, age, group, math_grade, pe_grade, it_grade])

    return students_base


def edit_info(student):
    show_base([student])
    process = int(input(
                        'Какую графу Вы хотите отредактировать?\n'
                        '1.Имя\n'
                        '2.Возраст\n'
                        '3.Группа\n'
                        '4.Математика\n'
                        '5.Физкультура\n'
                        '6.Информатика\n'
                        ))
    while process not in range(1, 6):
        process = int(input('Выберите редактируемый параметр из списка'))
    if process == 1 or process == 3:
        new_data = input('Введите новый параметр:\n')
    else:
        new_data = int(input('Введите новый параметр:\n'))
    student[process-1] = new_data

    return student


def show_info(student):
    average = average_calc([gr for gr in student[3:] if gr is not None])
    student_info = [*student[:3], average]
    print(
        f"Имя: {student_info[0]}\n"
        f"Возраст: {student_info[1]}\n"
        f"Группа: {student_info[2]}\n"
        f"Средняя оценка: {average:.2f}"
    )
    return student_info


def main():
    length = int(input('Введите количество генерируемых студентов: '))
    students_base = create_rand_base(length)
    show_base(students_base)

    while True:
        process = int(input('Выберите действие: \n'
                            '1. Вывести информацию о выбранном студенте \n'
                            '2. Ввести данные нового студенте  \n'
                            '3. Редактировать данные студента из базы \n'))
        while process not in range(1, 4):
            process = int(input('Пожалуйста, выберите действие из списка: \n'
                                '1. Вывести информацию о выбранном студенте \n'
                                '2. Ввести данные нового студенте  \n'
                                '3. Редактировать данные студента из базы \n'))
        if process == 1:
            print('ИНФОРМАЦИЯ О СТУДЕНТЕ')
            student_number = int(input('Введите номер студента из списка: '))
            show_info(students_base[student_number-1])
            print()

        if process == 2:
            print('СОЗДАНИЕ НОВОГО СТУДЕНТА')
            students_base = insert_info(students_base)
            show_base(students_base)
            print()

        if process == 3:
            print('РЕДАКТИРОВАНИЕ ДАННЫХ СТУДЕНТА')
            student_number = int(input('Выберите номер студента для редактирования: '))
            edit_info(students_base[student_number-1])
            show_base(students_base)
            print()


main()

