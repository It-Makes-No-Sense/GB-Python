# Требуется вывести все целые степени двойки ( не превосходящие числа N.т.е. числа вида 2^k),

def two(n):
    m = 1
    while m < n:
        print(m, end=' ')
        m = m * 2

n = int(input("Введите число: "))
two(n)