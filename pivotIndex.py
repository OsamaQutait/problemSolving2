from typing import *
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        total_sum = sum(nums)
        for i in range(len(nums)):
            if left_sum == total_sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        return -1

if __name__ == '__main__':
    nums = [1, 7, 3, 6, 5, 6]
    solution = Solution()
    print(solution.pivotIndex(nums))