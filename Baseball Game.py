from typing import *
def calPoints(operations: List[str]) -> int:
    stack = []
    for operation in operations:
        if operation == '+':
            stack.append(stack[-1]+stack[-2])
        elif operation == 'D':
            stack.append(stack[-1]*2)
        elif operation == 'C':
            stack.pop()
        else:
            stack.append(int(operation))
    return sum(stack)

if __name__ == '__main__':
    print(calPoints(["5","2","C","D","+"]))
