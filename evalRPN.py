from typing import *
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op_set = {"*", "/", "+", "-"}
        for x in tokens:
            if x not in op_set:
                stack.append(int(x))
            else:
                if x == "+":
                    stack.append(stack.pop() + stack.pop())
                elif x == "*":
                    stack.append(stack.pop() * stack.pop())
                elif x == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))
                elif x == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
        return stack[0]

if __name__ == '__main__':
    tokens = ["4","3","-"]
    solution = Solution()
    print(solution.evalRPN(tokens))
