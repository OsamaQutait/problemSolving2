from typing import *
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0]*len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                answer[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
        return answer


if __name__ == '__main__':
    temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
    solution = Solution()
    print(solution.dailyTemperatures(temperatures))