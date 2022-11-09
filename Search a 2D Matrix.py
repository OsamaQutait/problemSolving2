from typing import List
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    row, col = len(matrix), len(matrix[0])
    for i in range(row):
        if matrix[i][col-1] >= target:
            l, r = 0, col-1
            while l <= r:
                mid = l + (r - l) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
    return False

if __name__ == '__main__':
    print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))