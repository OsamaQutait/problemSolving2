def twoSum(numbers, target):
    a_pointer = 0
    b_pointer = len(numbers) - 1
    while True:
        if numbers[a_pointer] + numbers[b_pointer] == target:
            return [a_pointer + 1, b_pointer + 1]
        elif numbers[a_pointer] + numbers[b_pointer] > target:
            b_pointer -= 1
        elif numbers[a_pointer] + numbers[b_pointer] < target:
            a_pointer += 1


if __name__ == '__main__':
    print(twoSum([-1, 0], -1))

