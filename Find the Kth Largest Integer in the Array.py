from typing import *
def kthLargestNumber(nums: List[str], k: int) -> str:
    nums = [int(num) for num in nums]
    nums.sort(reverse=True)
    return str(nums[k-1])

if __name__ == '__main__':
    print(kthLargestNumber(["3", "6", "7", "10"], 4))
