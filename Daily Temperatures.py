from typing import *
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    answer = [0] * len(temperatures)
    stack = []
    for i, temp in enumerate(temperatures):
        while stack and temp > stack[-1][0]:
            t, e = stack.pop()
            answer[e] = i - e
        stack.append([temp, i])
    return answer

if __name__ == '__main__':
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))