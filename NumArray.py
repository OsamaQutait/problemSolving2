from typing import *


class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        current_sum = 0
        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right] - 0
        else:
            return self.prefix[right] - self.prefix[left - 1]


if __name__ == '__main__':
    input_commands = ["NumArray", "sumRange", "sumRange", "sumRange"]
    input_data = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]

    num_array = None
    result = []

    for i in range(len(input_commands)):
        command = input_commands[i]
        data = input_data[i]

        if command == "NumArray":
            num_array = NumArray(data[0])
        elif command == "sumRange":
            result.append(num_array.sumRange(data[0], data[1]))

    print(result)
