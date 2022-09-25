from typing import *
def plusOne(digits: List[int]) -> List[int]:
    size = len(digits) - 1
    sum = digits[size] + 1
    if sum < 10:
        digits[size] = sum
    else:
        while sum == 10:
            digits[size] = 0
            size -= 1
            sum = digits[size] + 1
        if sum < 10 and size >= 0:
            digits[size] = sum
        elif sum < 10 and size < 0:
            digits.insert(0, 1)
        else:
            digits.insert(size, 1)
    return digits

def test_plusOne():
    digits = [8,9,9]
    answer = [9,0,0]
    assert plusOne(digits) == answer


if __name__ == '__main__':
    x = [1,5,3]
    x.insert(2, 25)
    print(x)