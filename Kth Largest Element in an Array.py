from typing import *
def findKthLargest(nums: List[int], k: int) -> int:
    nums = sorted(nums, reverse=True)
    return nums[k-1]

if __name__ == '__main__':
    print(findKthLargest([3,2,3,1,2,4,5,5,6], 4))