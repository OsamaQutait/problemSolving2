from typing import *
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        l, r = 0, k-1
        res = float("inf")
        while r < len(nums):
            res = min(nums[r]-nums[l], res)
            l += 1
            r += 1
        return res

if __name__ == '__main__':
    nums = [9,4,1,7]
    k = 2
    solution = Solution()
    print(solution.minimumDifference(nums, k))