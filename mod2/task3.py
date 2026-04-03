#Выведите число, которое будет стоять между двумя другими после упорядочивания.
# Считываем строку с входными данными (ожидается формат "число число число")
input_string = input()

# Находим индекс первого пробела, чтобы отделить первое число
index_first_space = input_string.find(" ")

# Вырезаем подстроку до первого пробела и преобразуем её в целое число
first_number = int(input_string[:index_first_space])

# Обновляем строку, убирая из неё уже прочитанное первое число и пробел
input_string = input_string[index_first_space+1:]
# Находим индекс следующего пробела
index_second_space = input_string.find(" ")

# Вырезаем второе число (между первым и вторым пробелом в исходной строке)
second_number = int(input_string[:index_second_space])
# Всё, что осталось после второго пробела — это третье число
third_number = int(input_string[index_second_space+1:])

# --- Блок первичной сортировки первых двух чисел ---
if first_number < second_number:
    min = first_number      # Меньшее из первых двух
    middle = second_number   # Большее из первых двух
elif second_number < first_number:
    min = second_number
    middle = first_number

# --- Блок поиска итогового среднего числа с учетом третьего ---
if middle < third_number:
    # Если третье число самое большое, то средним остается middle
    result = middle
elif (third_number < middle) and (third_number > min):
    # Если третье число зажато между min и middle, то оно и есть среднее
    result = third_number
elif third_number < min:
    # Если третье число самое маленькое, то средним становится min
    result = min

# Вывод итогового среднего числа
print(f"{result}")
