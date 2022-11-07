import operator
from typing import *
def evalRPN(tokens: List[str]) -> int:
    operation_dict = {
        ''
        '+': operator.add,
        '-': operator.sub,
        '/': operator.truediv,
        '*': operator.mul
    }
    stack = []
    for item in tokens:
        if operation_dict.__contains__(item):
            answer = int(operation_dict.get(item)(int(stack[-2]), int(stack[-1])))
            stack.pop()
            stack.pop()
            stack.append(answer)
        else:
            stack.append(item)
    return stack[-1]

if __name__ == '__main__':
    print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))

