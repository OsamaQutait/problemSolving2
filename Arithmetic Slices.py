from typing import *
def numberOfArithmeticSlices(nums: List[int]) -> int:
    if len(nums) < 3:
        return 0
    helper_array = [0] * len(nums)
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            helper_array[i] = 1 + helper_array[i-1]
    return sum(helper_array)

if __name__ == '__main__':
    print(numberOfArithmeticSlices([1]))