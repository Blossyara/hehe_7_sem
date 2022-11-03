# Домашнее задание 4 (21.09.2022):
# Сделать программу, которая визуализирует в консоли окружность заданного диаметра с центром в указанных координатах.
# В том случае, если окружность выходит за границы поля сообщить об этом и ничего не рисовать.


def create_field(n):
    field = []
    for i in range(n):
        field.append([0] * n)
    return field


def display_field(field):
    for y in range(len(field)):
        print(field[y])


def range_check(d, n, x_centre, y_centre):
    if (x_centre - (d-1)/2 < 0 or y_centre + (d-1)/2 > n or y_centre - (d-1)/2 < 0 or y_centre + (d-1)/2 >= n
            or x_centre > n or y_centre > n):
        return False
    else:
        return True


def display_circle(field, x_centre, y_centre, d):
    for y in range(len(field)):
        for x in range(len(field[y])):
            if (x-x_centre)**2 + (y-y_centre)**2 <= ((d-1)/2)**2:
                field[y][x] = 1
                break
        for x in range(len(field[y]), 1, -1):
            if (x-x_centre)**2 + (y-y_centre)**2 <= ((d-1)/2)**2:
                field[y][x] = 1
                break
    for x in range(len(field)):
        for y in range(len(field[x])):
            if (x-x_centre)**2 + (y-y_centre)**2 <= ((d-1)/2)**2:
                field[y][x] = 1
                break
        for y in range(len(field[x]), 1, -1):
            if (x-x_centre)**2 + (y-y_centre)**2 <= ((d-1)/2)**2:
                field[y][x] = 1
                break
    field[y_centre][x_centre] = 1
    display_field(field)
    return field


def main():
    n = int(input('Введите размер квадратного поля NxN: '))
    field = create_field(n)
    display_field(field)

    rng_check = False
    while rng_check is False:
        x_input = int(input('Введите координату центра по Х: ')) - 1
        y_input = int(input('Введите координату центра по Y: ')) - 1
        d = int(input('Введите диаметр окружности (нечетное значение): '))
        while d % 2 == 0 and d < 1:
            d = int(input('Введите, пожалуйста, положительное нечетное значения для диаметра окружности: '))
        rng_check = range_check(d, n, x_input, y_input)
        if not rng_check:
            print('Невозможно построить окружность с заданными параметрами центра и диаметра. \n', )

    display_circle(field, x_input, y_input, d)


main()
