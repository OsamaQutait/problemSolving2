from typing import *
def rotate(nums: List[int], k: int) -> None:
    a_pointer = len(nums) - 1
    temp = nums[a_pointer]
    while k:
        nums.pop()
        nums.insert(0, temp)
        k -= 1
        temp = nums[a_pointer]
    return nums

if __name__ == '__main__':
    print(rotate([-1,-100,3,99], 2))

