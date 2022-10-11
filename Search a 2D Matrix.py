from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    rowSize, columnSize = len(matrix[0]), len(matrix)
    for i in range(columnSize):
        print(matrix[i][rowSize-1])
    return True

if __name__ == '__main__':
    print(searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))