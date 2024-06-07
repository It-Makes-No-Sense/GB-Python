from array import array, typecodes

print(typecodes)  # Всевозможные буквы для создания array

long_array = array('l', [-6000, 800, 100500])  # l - целое со знаком, 4 байта
print(long_array)
long_array.append(2 ** 32)  # OverflowError
long_array.append(3.14)  # TypeError
