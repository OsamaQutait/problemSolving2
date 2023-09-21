from typing import *
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
        print(nums)


if __name__ == '__main__':
    nums = [2, 1]
    solution = Solution()
    print(solution.moveZeroes(nums))