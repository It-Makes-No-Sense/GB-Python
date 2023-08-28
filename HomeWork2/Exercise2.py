"""
Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
а Катя должна их отгадать. Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
"""
import random
from math import sqrt


def what_number(S, P):
    d = S * S - 4 * P
    if d > 0:
        sq = sqrt(d) / 2
        b = S / 2
        x = int(b - sq)
        y = int(b + sq)
        print(f"y:{y} x:{x} sum:{S} mul:{P}")
    elif d == 1:
        x, y = S / 2
        print(f"y:{y} x:{x} sum:{S} mul:{P}")


num1 = random.randint(1, 1000)
num2 = random.randint(1, 1000)
print(num1, num2)
what_number(num1 + num2, num2 * num1)
