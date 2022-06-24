# 1 -  Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный. Функцию eval не использовать!
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Дополнительно: Добавить возможность использования скобок, меняющих приоритет операций.
# Пример: 1+2*3 => 7; (1+2)*3 => 9_seminar;

print('Задача № 1')

#  оператор: (приоритет операции, производимое вычисление)

OPERATORS = {
    '+': (1, lambda x, y: x + y),
    '-': (1, lambda x, y: x - y),
    '*': (2, lambda x, y: x * y),
    '/': (2, lambda x, y: x / y)
}

# перводим строковое выражение в массив чисел и операторов, следующих в том же порядке
def expression_to_infixlist(math_expression):
    infix = []
    number = ''
    for s in math_expression:
        if s.isdigit():
            number += s
        else: # если символ не цифра, то выдаём собранное число и начинаем собирать заново
            infix.append(float(number))
            number = ''
        if s in OPERATORS: # если символ - оператор, то выдаём как есть
            infix.append(s)
    if number:  # если в конце строки есть число, выдаём его
        infix.append(float(number))
    return infix


# Сортируем массив цифр и операторов в постфиксное представление (польская нотация).
def sort_polish(infix):
    postfix = []
    stack = []
    for token in infix:
        if token in OPERATORS:
            while stack and OPERATORS[token][0] <= OPERATORS[stack[-1]][0]: # пока стек не пуст и приоритет текущего оператора
                                                                            # меньше либо равен последнему записанному в стек
                                                                            # оператору в основной масив добавляется последний
                                                                            # оператор из стека в обратном случае текущий
                                                                            # оператор записывается в стек
                postfix.append(stack.pop())
            stack.append(token)
        else:
            postfix.append(token)
    while stack:
        postfix.append(stack.pop())
    return postfix


# Вычисляем мат. выражение в польской нотации.
def calc(polish):
    stack = []
    for token in polish:
        if token in OPERATORS:  # если приходящий элемент - оператор,
            y, x = stack.pop(), stack.pop()  # забираем 2 числа из стека
            stack.append(OPERATORS[token][1](x, y)) # вычисляем оператор, результат возвращаем в стек
        else:
            stack.append(token)
    return stack[0] # результат вычисления - единственный элемент в стеке


# Вычисляет мат. выражение с помощью польской нотации.
def calc_math_expression(math_expression):
    polish_infix = expression_to_infixlist(math_expression)
    polish = sort_polish(polish_infix)
    return calc(polish)

math_expression = '10+62-15*2+6/10'

res = calc_math_expression(math_expression)
print(res)

# алгоритм честно взят у Адиля, на самостоятельные поиски потрачено много времени безрезультатно

# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных файлах (в одном файлике отрывок из какой-то книги,
# а втором файлике — сжатая версия этого текста).

print('Задача № 2')

#работа с файлами

def read_text_from_file(file_name):
    file = open(file_name, 'r')
    data = file.read()
    file.close()
    return data

def write_text_in_file(file_name, text):
    file = open(file_name, 'w')
    file.write(text)
    file.close()


#кодирование
def rle_encode(data):
    encoded = []
    count = 1
    for i in range(len(data)):
        if i == len(data) - 1:  #проверка на последний символ, чтобы не выйти за пределы массива
            encoded.append(str(count))
            encoded.append(data[i])
        elif data[i] == data[i + 1]:     # если текущий символ равен следующему считаем количество повторов
            count += 1
        else:                            # когда повторы заканчиваются записываем их количество и сам символ
            encoded.append(str(count))
            encoded.append(data[i])
            count = 1
    return ''.join(encoded)              # переводим полученный список в строку


# раскодирование
def rle_decode(data):
    decoded = []
    number = 0
    for i in range(len(data)):
        if data[i].isdigit():
            number = number * 10 + int(data[i])   #собираем число: '12' = iter1 (0*10+1), iter2 (1*10+2) = 12
        else:
            decoded.append(data[i] * number)      #символ умножаем на число: 'A'*3 = 'AAA'
            number = 0                            # обнуляем number
    return ''.join(decoded)                       # перевод результата в строку


input_text = read_text_from_file('input_text_rle.txt')
output_text = rle_encode(input_text)
print("Исходный текст: ", input_text)
print("Кодированный текст: ", output_text)
write_text_in_file('output_text_rle.txt', output_text)
print("Раскодированный текст: ", rle_decode(output_text))


# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, которая идет через 13 букв после нее
# в алфавите. ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 .
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. Также создайте функцию,
# которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений).
# Не использовать функцию encode.

def rot13(text, decode=False):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in text:
        if i in alphabet:
            if decode:
                result += alphabet[(alphabet.index(i) - 13) % 26]     #особенности остатков от деления отрицательных чисел стали большим открытием
            else:                                                     #в данном случае это позволяет оставаться в границах строки заменяя отрицательные индексы соответствующими положительными
                result += alphabet[(alphabet.index(i) + 13) % 26]
        else:
            result += i
    return result

input_text = "hi mister Anderson, i am agent Smith № 321"
print("input_text=", input_text)
encode_text = rot13(input_text)
print("encode_text=", encode_text)
decode_text = rot13(encode_text, decode=True)
print("decode_text=", decode_text)