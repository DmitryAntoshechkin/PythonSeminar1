# Задача 2: - HARD необязательная, идет за 3 обязательных 
# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. 
# Через строку решать нельзя.

from decimal import Decimal
try:
    number = Decimal (input('Введите число: '))
    if number < 0:
        number = -number
    while number != number.quantize(Decimal("1")): #Убираем друбную часть
        number *= 10
    number = int(number)
    sum = 0
    while number > 0:  #Считаем сумму цифр
        sum += number % 10
        number //= 10
    print('Сумма цифр:',sum)
except:
    print('Введены некорректные данные')