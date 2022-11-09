from typing import *
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    def binarySearch(arr, l, r, x):
        while l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return True
            elif arr[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return False
    row, col = len(matrix), len(matrix[0])
    for i in range(0, col):
        if (matrix[0][i] <= target) and (matrix[row-1][i] >= target):
            arr = [matrix[x][i] for x in range(row)]
            if binarySearch(arr, 0, len(arr)-1, target):
                return True
        if (matrix[0][i] > target) and (matrix[row-1][i] > target):
            break
    return False

if __name__ == '__main__':
    print(searchMatrix([[-1],[-1]],-1))