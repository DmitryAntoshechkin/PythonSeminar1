# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

try:
    number = int (input('Введите шестизначный номер билета: '))
    if number < 100000 or number > 999999:
        print('Введено некорректное число')
    else:
        sum1 = 0
        for i in range(0,3):
            sum1 += number % 10
            number //= 10
        sum2 = 0
        for i in range(0,3):
            sum2 += number % 10
            number //= 10
        if sum1 == sum2:
            print('Ура! Счастливый билет!')
        else:
            print('Повезет в другой раз')
except:
    print('Введены некорректные данные')