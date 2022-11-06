from typing import *
from collections import *
import numpy as np
def minOperations(grid: List[List[int]], x: int) -> int:
    if not grid:
        return -1
    grid = sorted(list(np.array(grid).flatten()))
    flag = True if len(Counter([num % x for num in grid])) == 1 else False
    if not flag:
        return -1
    else:
        if len(grid) % 2 == 0:
            number_of_operation = [0, 0]
            middle = grid[len(grid) // 2]
            for num in grid:
                number_of_operation[0] += abs(num - middle) // x
            middle = grid[(len(grid) // 2)-1]
            for num in grid:
                number_of_operation[1] += abs(num - middle) // x
            return min(number_of_operation)
        else:
            middle = grid[len(grid) // 2]
            number_of_operation = 0
            for num in grid:
                number_of_operation += abs(num - middle) // x
            return number_of_operation

if __name__ == '__main__':
    # print((open("t", "r").read()))
    print(minOperations([], 1))