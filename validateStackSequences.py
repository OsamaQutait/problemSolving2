from typing import *
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        i = 0
        for num in pushed:
            stack.append(num)
            while i < len(popped) and stack[-1] == popped[i]:
                stack.pop()
                i += 1
                if len(stack) == 0:
                    break
        return len(stack) == 0


if __name__ == '__main__':
    pushed = [1, 0]
    popped = [1, 0]
    solution = Solution()
    print(solution.validateStackSequences(pushed, popped))
