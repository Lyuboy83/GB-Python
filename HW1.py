# Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# n = int(input("Введите трёхзначное число: "))
# a = n // 100
# b = n // 10 % 10
# c = n % 10
# res = a + b + c
# print("Первая цифра", a, "Вторая цифра", b,
#       "Третья цифра", c, "Сумма цифр",  res)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# S = int(input("Введите общее число журавликов(кратное 6): "))
# Petya = int(S / 6)
# Katya = int(S / 6 * 4)
# Seryoja = int(S / 6)
# print(Petya, Katya,  Seryoja)

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

# t = int(input("Введите шестизначное число: "))
# a = t // 100000
# b = t // 10000
# c = t // 1000
# d = t // 100
# e = t // 100 % 10
# f = t % 10
# a1 = a + b + c
# b1 = d + e + f
# if a1 == b1:
#     print(a, b, c, d, e, f, a1, b1, 'yes')
# else:
#     print(a, b, c,  d, e,  f,  a1, b1,  'no')


# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no
