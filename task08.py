# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

try:
    n = int (input('Введите первый размер: '))
    m = int (input('Введите второй размер: '))
    k = int (input('Сколько долек ломаем: '))
    if n < 1 or m < 1 or k < 1:        
        print('Введен неверный размер')
    else:
        if (k % n == 0 or k % m == 0) and k < m * n :
            print('Можно отломить')
        else:
            print('Нельзя отломить')
except:
    print('Введены некорректные данные')