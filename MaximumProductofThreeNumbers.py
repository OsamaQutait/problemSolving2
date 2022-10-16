from typing import *
def maximumProduct(nums: List[int]) -> int:
    length = len(nums) - 1
    nums = sorted(nums)
    return max(nums[length]*nums[length-1]* nums[length-2],  nums[0]* nums[1]* nums[length])

if __name__ == '__main__':
    print(maximumProduct(
[1,2,3]))
