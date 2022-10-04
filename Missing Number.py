from typing import *
def missingNumber(nums: List[int]) -> int:
    numsLen = len(nums)
    sumList = sum(nums)
    realSum = numsLen*(numsLen + 1) // 2
    return realSum - sumList

if __name__ == "__main__":
    print(missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
