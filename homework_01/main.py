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
    mas = 0
    for i in range(len(nums)):
        mas[i] = nums[i] * nums[i]
    return mas
# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(nums, type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    mas = 0
    if type == ODD:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                mas[j] = nums[i]
            j += 1
    elif type == EVEN:
        j = 0
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                mas[j] = nums[i]
            j += 1
    else:
        for i in range(len(nums)):
            for k in range(nums[i]):
                if nums[i]/k == 0 and k != nums[i]:
                    break
                if nums[i]/k == 0 and k == nums[i]:
                    mas[j] = nums[i]
            j += 1
