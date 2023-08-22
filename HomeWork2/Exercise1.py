"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть
"""
import random


def coins(cnt):
    try:
        cnt = int(cnt)
        cnt_reshka = 0
        for i in range(1, cnt + 1):
            reshka = random.randint(0, 1)
            if reshka:
                cnt_reshka += 1
        cnt_orel = cnt - cnt_reshka

        print(f"Орлы:{cnt_orel}, Решки {cnt_reshka}")

        if cnt_orel >= cnt_reshka:
            print(cnt_reshka)
        else:
            print(cnt_orel)
    except:
        print('Это не число!!')


coins(input('Введите кол-во монет'))
