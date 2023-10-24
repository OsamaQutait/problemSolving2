from collections import deque

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        for _ in range(len(self.q1)):
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1) == 0

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(8)
obj.push(6)
obj.push(55)
obj.push(5)
obj.push(577)
obj.push(854)

# Print the top element
param_3 = obj.top()
print("Top element:", param_3)

param_2 = obj.pop()
print(param_2)
param_3 = obj.top()
print(param_3)
param_4 = obj.empty()
print(param_4)