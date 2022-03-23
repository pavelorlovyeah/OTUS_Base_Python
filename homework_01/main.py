"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(nums):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return nums ** 2

# Text below just for function testing check
# nums = (1, 2, 3, 4, 5)
# print(list(map(power_numbers, nums)))



#filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(numbers):
        if numbers > 1:
            for num in range(2, round(numbers ** 0.5) + 1):
                if numbers % num == 0:
                    return()
            return numbers


def is_odd(numbers):
    if numbers % 2 == 0:
        return numbers


def is_even(numbers):
    if numbers % 2 != 0:
        return numbers

# Text below just for function testing check
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
# print(list(filter(is_odd, numbers)))


def filter_numbers(numbers, numbers_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if numbers_type == EVEN:
        return list(filter(is_even, numbers))
    if numbers_type == ODD:
        return list(filter(is_odd, numbers))
    if numbers_type == PRIME:
        return list(filter(is_prime, numbers))

# Text below just for function testing check
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# numbers_type = PRIME
# print(filter_numbers(numbers, numbers_type))