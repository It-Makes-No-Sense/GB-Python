# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном списке урожайности грядки.

N = int(input('Введите кол-во кустов'))
a = [int(input(f'Количество ягод на {i} кусте')) for i in range(1, N + 1)]
max = 0
for i in a:
    if a.index(i) == 0:
        cnt = a[-1] + i + a[a.index(i) + 1]
        if cnt > max:
            max = cnt
    elif a.index(i) == len(a) - 1:
        cnt = a[0] + i + a[a.index(i) - 1]
        if cnt > max:
            max = cnt
    else:
        cnt = a[a.index(i) - 1] + i + a[a.index(i) + 1]
        if cnt > max:
            max = cnt
print(max)