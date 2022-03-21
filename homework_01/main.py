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

#uncomment for cross-check
#nums = (1, 2, 3, 4, 5)
#print(list(map(power_numbers, nums)))



#filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(*nums, nums_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if nums_type == "ODD":
        return nums % 2 != 0
    if nums_type == "EVEN":
        return nums % 2 == 0
    if nums_type == "PRIME":
        if nums > 1:
           for num in range(2, round(nums ** 0.5) + 1):
            if nums % num == 0:
                return()
           return nums

nums = ((1,2,3,4,5,6,7,8,9,10), "ODD")


list(filter(filter_numbers, nums))

