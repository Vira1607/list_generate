# Генерация списка

# Дано целое число N. Программа формирует список из нечётных чисел от 1 до N.

number_first = 1
number_last = int(input('Введите число N: '))
list_of_numbers = []

while number_first <= number_last:
  list_of_numbers.append(number_first)
  number_first += 2

print(list_of_numbers)
