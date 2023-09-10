# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows=6, num_columns=6):
    res = []
    for i in range(1, num_rows + 1):
        res.append([i])
        for j in range(2, num_columns + 1):
            if i == 1:
                res[i - 1].append(j)
            else:
                res[i - 1].append(operation(i, j))
    for i in res:
        line = ' '.join(list(map(str, i)))
        print(line)


print_operation_table(lambda x, y: x * y)
