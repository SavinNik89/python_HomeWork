# 1. Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4
import math
import random

print('Задача № 1')


def sum_not_even_position(numbers):
    sum_pos = 0
    for i in range(1, len(numbers)):
        if i % 2 != 0:
            sum_pos += numbers[i]
    return sum_pos


numbers = [2, 3, 5, 9, 8, 1, 15, 5, 9, 10]
print(f'Исходный массив: {numbers}')
print(f'Сумма значений на нечетных позициях: {sum_not_even_position(numbers)}')

# 2. Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15] 

print('Задача № 2')


def mult_couple(nums):
    result_array = []
    for i in range((len(nums) // 2)):
        mult = nums[i] * nums[len(nums) - 1 - i]
        result_array.append(mult)
    if len(nums) % 2 != 0:
        result_array.append(nums[(len(nums) // 2)] ** 2)
    return result_array


nums = [2, 3, 4, 5, 6, 7, 8, 9]
print(f'Исходный массив: {nums}')
print(f'Произведения пар чисел: {mult_couple(nums)}')

# 3. В заданном списке вещественных чисел найдите разницу между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Задача № 3')


def found_min_numb(array):
    min_num = array[0]
    for i in range(1, len(array)):
        if array[i] < min_num and array[i] != 0:
            min_num = array[i]
    return min_num


def found_max_numb(array):
    max_num = array[0]
    for i in range(1, len(array)):
        if array[i] > max_num:
            max_num = array[i]
    return max_num


def min_max_fractional_part(float_nums):
    temp_list = []
    for i in range(len(float_nums)):
        temp_list.append(round(float_nums[i] % 1, 3))
    print(f'Максимальная дробная часть: {found_max_numb(temp_list)}')
    print(f'Минимальная дробная часть: {found_min_numb(temp_list)}')
    result = found_max_numb(temp_list) - found_min_numb(temp_list)
    return result


array = [1.1, 1.2, 3.1, 5, 10.01]
print(f'Исходный массив: {array}')
print(f'Разница между максимальной и минимальной дробной частью: {min_max_fractional_part(array)}')

# 4. Написать программу преобразования десятичного числа в двоичное
#

print('Задача № 4')


def dec_to_double(dec_num):
    double_num = ''
    temp = dec_num
    if dec_num < 0:  # проверка на отризательность
        dec_num += -2 * dec_num  # избавляемся от минуса, так либо можно и через abs()
    while dec_num > 0:  # собираем остатки от деления в двоичное число
        double_num = str(dec_num % 2) + double_num
        dec_num = dec_num // 2
    double_num = '0' + double_num  # добавляем знаковый разряд "0" для положительного числа
    if temp < 0:
        neg_double_num = []  # создаем список для записи инвертированных цифр
        for i in double_num:  # записываем инверсию в список
            if i == '0':
                neg_double_num.append('1')
            else:
                neg_double_num.append('0')
        double_num = ''.join(neg_double_num)
    return double_num


dec_num = int(input('Введите число в десятичной системе: '))
print(f'Число в двоичной системе (со знаковым разрядом): {dec_to_double(dec_num)}')

# Либо так:
print(bin(dec_num))

# Экстра-задачи:
# 1. Написать программу преобразования двоичного числа в десятичное.
#
print('Задача № 5 (1*)')


def double_to_dec(doub_num):
    digits_list = list(doub_num)
    dec_num = 0
    for i in range(len(digits_list)):
        dec_num += int(digits_list[len(digits_list) - 1 - i]) * 2 ** i
        i += 1
    return dec_num


def input_num():
    while True:
        doub_num = input('Введите число в двоичной системе: ')
        count = 0
        for i in doub_num:
            if i != '1' and i != '0':
                count += 1
        if count != 0:
            print('Число в двоичной системе может состоять только из 1 и 0, повторите ввод корректно')
        else:
            break
    return doub_num


doub_num = input_num()
print(f'Введенное двоичное число: {doub_num}')
dec_num = double_to_dec(doub_num)
print(f'Полученное десятичное число: {dec_num}')

# p.s. будем считать, что все двоичные будут положительными)))


# 2. Создайте программу, которая будет играть в игру “коровы и быки” с пользователем. Игра работает так:
#
# Случайным образом генерируйте 4-значное число. Попросите пользователя угадать 4-значное число. За каждую цифру,
# которую пользователь правильно угадал в нужном месте, у них есть “корова”. За каждую цифру, которую пользователь
# угадал правильно, в неправильном месте стоит “бык”. Каждый раз, когда пользователь делает предположение, скажите им,
# сколько у них “коров” и “быков”. Как только пользователь угадает правильное число, игра окончена. Следите за количеством
# догадок, которые пользователь делает на протяжении всей игры, и сообщите пользователю в конце.

print('Задача № 6 (2*)')

quest_number = str(random.randint(1000, 9999))
print(quest_number)
print('Ваша задача угадать загаданное четырехзначное число')
n = 0
while True:
    answer_number = input('Введите четырехзначное число (игра быки и коровы): ')
    if len(answer_number) != 4:
        print('Вводимое значение должно быть четырехзначным, повторите ввод корректно!')
        continue
    n += 1
    bull = 0
    cow = 0
    for i in range(4):
        if answer_number[i] == quest_number[i]:
            bull += 1
        elif answer_number[i] in quest_number:
            cow += 1
    if bull == 4:
        print(f'Вы угадали за {n} попыток! Победа ваша')
        break
    else:
        print(f'В числе {answer_number} {bull} быка и {cow} коров, пробуйте еще!')

# p.s. в оригинальной версии игры есть одно важное условие: цифры в числе не могут повторяться, иначе процесс угадывания
# сильно осложняется - количество коров, как в данном случае, становиться неинформативно


# 3.Каждый следующий элемент ряда Фибоначчи получается при сложении двух предыдущих. Начиная с 1 и 2, первые 10 элементов будут:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# Найдите сумму всех четных элементов ряда Фибоначчи, которые не превышают четыре миллиона.

print('Задача № 7 (3*)')


def fibo_list(max):
    next_num = 0
    fibo = [1, 2]
    while True:
        i = len(fibo) - 1
        j = len(fibo) - 2
        next_num = fibo[i] + fibo[j]
        if next_num > max:
            break
        fibo.append(next_num)
    return fibo


def sum_even_numbers(fibo):
    sum_numbers = 0
    for i in fibo:
        if i % 2 == 0:
            sum_numbers += i
    return sum_numbers


fibo = fibo_list(4000000)
print(fibo)
print(f'Сумма четных чисел фибоначчи, не превышающих 4.000.000 = {sum_even_numbers(fibo)}')

# 4. Простые делители числа 13195 - это 5, 7, 13 и 29.
# Каков самый большой делитель числа 600851475143, являющийся простым числом?

print('Задача № 8 (4*)')


# def found_divis(number):
#     divisors = []
#     for i in range(2, int(math.sqrt(number))+1):        # простые делители не могут превышать значение корня из делимого (без данного ограничения вычисления очень долгие)
#         if number % i == 0:
#             divisors.append(i)
#     return divisors
#
#
# def simple_divisors(divisors):
#     simple_div = []
#     for d in divisors:
#         count = 0
#         for j in range(2, d//2+1):
#             if d % j == 0:
#                 count += 1
#         if count == 0:
#             simple_div.append(d)
#     return simple_div
#
#
# number = 600851475143
# divisors = found_divis(number)
# print(f'Все делители: {divisors}')
# simple_div = simple_divisors(divisors)
# print(f'Простые делители: {simple_div}')
# max_div = found_max_numb(simple_div)
# print(f'Максимальный простой делитель: {max_div}')

def simple_num(number):
    count = 0
    for j in range(2, number // 2 + 1):
        if number % j == 0:
            count += 1
    if count == 0:
        return True
    else:
        return False


def found_divis(number):
    divisors = []
    for i in reversed(range(2, int(math.sqrt(number)) + 1)):
        if number % i == 0 and simple_num(i) is True:
            break
        else:
            continue
    return i


number = 600851475143
print(f'Наибольший простой делитель {number} = {found_divis(number)}')





# 5. 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.Какое самое маленькое число делится
# нацело на все числа от 1 до 20?

print('Задача № 9_seminar (5*)')


def simple_num(numbers):
    simple_num = []
    for d in numbers:
        count = 0
        for j in range(2, d // 2 + 1):
            if d % j == 0:
                count += 1
        if count == 0:
            simple_num.append(d)
    return simple_num


def found_div(number):
    divisors = []
    for i in range(2, number // 2):
        if number % i == 0:
            divisors.append(i)
    return divisors


N = 21                                  #делаем решение для последовательности чисел от 1 до N-1, здесь задаем N
temp_prod = 1
result = 1

input_numbers = list(range(1, N))
div = simple_num(input_numbers)         #все простые числа из последовательности выводим в отдельный список,
                                        # далее этот список будет основным для получения результата
# print(div)

notsimple_list = []                     #все непростые числа также формируем в отдельный список
for i in input_numbers:
    if i in div:
        continue
    else:
        notsimple_list.append(i)
# print(notsimple_list)

div.remove(1)                           #для дальнейших расчетов исключаем 1 из списка простых чисел

base_log = []
pov_log = []
for i in notsimple_list:                      #цикл проверяет является ли непростое число какой-либо степенью простого
    for j in div:                             #и записывает соответствующее простое число в один список, а его степень в другой,
        if (math.log(i, j)).is_integer():     #на соответствующих друг другу позициях
            base_log.append(j)
            pov_log.append(math.log(i, j))
# print(base_log)
# print(pov_log)

for i in base_log:                             #простые числа, степени которых найдены среди непростых чисел последовательности, удаляются
    for j in div:
        if i == j:
            div.remove(j)
# print(f'div {div}')

multip_list = []                                      #создается список, в котором номер позиции является простым числом, а значение
for m in range(0, found_max_numb(base_log)+1):        #а значение элемента на данной позиции его максимальной степенью, встречающейся в заданной
    multip_list.append(1)                             #последовательности
for n in range(0, len(base_log)):
    if multip_list[base_log[n]] < pov_log[n]:
        multip_list[base_log[n]] = pov_log[n]
# print(multip_list)



for i in range(1, len(multip_list)):               #находится произведение найденых максимальных степеней простых чисел
    if multip_list[i] != 1:
        max_pow = i**multip_list[i]                    #и добавляется в основной список div
        temp_prod *= max_pow
div.append(temp_prod)

for i in div:                                       #находим произведение всех элементов списка div, что и будет искомым ответом
    result = result * i
print(f'Наименьшее общее кратное чисел от 1 до {N-1}= {int(result)}')

print(f'Для проверки: {math.lcm(*range(1, N))}')
