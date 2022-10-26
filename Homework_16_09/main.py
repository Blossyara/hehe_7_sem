def isprime(number):
    if number % 2 == 0:
        return number == 2
    temp = 3
    while number % temp != 0 and temp * temp <= number:
        temp += 2
    return temp * temp > number


def show_list():
    is_shown = str.lower(input('Вывести список простых чисел?\n Да/Нет?\n'))
    if is_shown == "да":
        return True
    else:
        return False


def main():
    number = int(input("Введите число больше 2: "))
    while number <= 2:
        number = int(input("Пожалуйста, введите число больше 2: "))
    k = 0
    list_number = []
    for i in range(2, number+1):
        if isprime(i):
            k = i
            list_number.append(k)
    print("Последнее простое число:", k, '\n' 'Количество простых чисел в промежутке:', len(list_number))
    is_shown = show_list()
    if is_shown:
        for i in range(len(list_number)):
            print(f"{list_number[i]:7}", end='' if i % 20 != 19 else '\n')


main()
