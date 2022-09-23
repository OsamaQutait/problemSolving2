from typing import *
def findMaxConsecutiveOnes(nums: List[int]) -> int:
    max_local = 0
    max_global = 0
    size = len(nums) - 1
    for num in nums:
        if num == 0:
            max_global = max(max_global, max_local)
            max_local = 0
        else:
            max_local += 1
    max_global = max(max_global, max_local)
    return max_global

def test_findMaxConsecutiveOnes():
    nums = [1,0,1,1,0,1]
    answer = 2
    assert findMaxConsecutiveOnes(nums) == answer