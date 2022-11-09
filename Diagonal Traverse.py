from typing import *
def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
    i, j, m, n = 0, 0, len(mat), len(mat[0])
    answer = [0]*(m*n)
    for x in range(m*n):
        answer[x] = mat[i][j]
        if (i+j)%2 == 0: #up
            if j == n-1:
                i += 1
            elif i == 0:
                j += 1
            else:
                i -= 1
                j += 1
        else:#down
            if i == m-1:
                j += 1
            elif j == 0:
                i += 1
            else:
                i += 1
                j -= 1
    return answer
if __name__ == '__main__':
    print(findDiagonalOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
