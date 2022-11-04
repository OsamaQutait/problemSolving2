from typing import *
def thirdMax(nums: List[int]) -> int:
    nums = sorted(set(nums), reverse=True)
    try:
        return nums[2]
    except IndexError:
        return nums[0]


if __name__ == '__main__':
    print(thirdMax([3,2,3,1,2,4,5,5,6]))
