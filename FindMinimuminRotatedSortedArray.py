from typing import *
def findMin(nums: List[int]) -> int:
    start, end = 0, len(nums)-1
    while end > start:
        mid = (start+end)//2
        if nums[mid+1] < nums[mid]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        if nums[len(nums)-1] > nums[mid]:
            end = mid
        elif nums[len(nums)-1] < nums[mid]:
            start = mid

if __name__ == '__main__':
    print(findMin([11,13,15,17]))