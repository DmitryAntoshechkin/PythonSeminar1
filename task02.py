# Задача 2: Найдите сумму цифр трехзначного числа.

try:
    number = int (input('Введите трехзначное число: '))
    if number < 0:
        number = -number
    if number < 100 or number > 999:
        print('Введено не трехзначное число')
    else:
        sum = 0
        while number > 0:
            sum += number % 10
            number //= 10
        print('Сумма цифр:',sum)
except:
    print('Введены некорректные данные')
