from typing import *
def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    l, r = 0, k-1
    min_dif = nums[-1]
    while len(nums) > r:
        min_dif = min((nums[r] - nums[l]), min_dif)
        l += 1
        r += 1
    return min_dif

if __name__ == '__main__':
    print(minimumDifference([90], 1))