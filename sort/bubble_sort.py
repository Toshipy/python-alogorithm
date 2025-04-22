# [2, 5, 1, 8, 7, 3]
import random
from typing import List


def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
    tmp = 0
    for i in range(len_numbers):
        for j in range(len_numbers-1-i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                # tmp = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = tmp
    print(numbers)
    return numbers

if __name__ == '__main__':
    # nums = [2, 5, 1, 8, 7, 3]
    nums = [random.randint(0, 1000) for i in range(10)]
    bubble_sort(nums)