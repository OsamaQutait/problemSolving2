from typing import *
def generate(numRows: int) -> List[List[int]]:
    answer = []
    for i in range(numRows):
        answer.append([1]*(i+1))
        if len(answer[i]) > 2:
            for j in range(1, len(answer[i])-1):
                answer[i][j] = answer[-2][j] + answer[-2][j-1]
    return answer

if __name__ == '__main__':
    print(generate(3))