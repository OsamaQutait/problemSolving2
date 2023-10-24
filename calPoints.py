from typing import *
class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []
        ops_set = {"+", "D", "C"}
        for x in operations:
            if x not in ops_set:
                stack.append(int(x))
            else:
                if x == "+":
                    stack.append(stack[-1]+stack[-2])
                elif x == "D":
                    stack.append(2*stack[-1])
                elif x == "C":
                    stack.pop()
        return sum(stack)

if __name__ == '__main__':
    ops = ["5", "2", "C", "D", "+"]
    solution = Solution()
    print(solution.calPoints(ops))