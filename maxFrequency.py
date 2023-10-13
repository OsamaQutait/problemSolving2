from typing import *
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        l, r = 0, 0
        most_frequent_element = 0
        while r < len(nums):
            total += nums[r]
            while nums[r]*(r-l+1) > (total+k):
                total -= nums[l]
                l += 1
            most_frequent_element = max(most_frequent_element, r-l+1)
            r += 1
        return most_frequent_element

if __name__ == '__main__':
    nums = [1, 4, 8, 13]
    k = 5
    solution = Solution()
    print(solution.maxFrequency(nums, k))