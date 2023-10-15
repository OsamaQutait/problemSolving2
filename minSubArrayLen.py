from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        ans = float("inf")
        sum_nums = 0
        while r < len(nums):
            sum_nums += nums[r]
            while sum_nums >= target:
                ans = min(ans, r - l + 1)
                sum_nums -= nums[l]
                l += 1
            r += 1
        return ans if ans != float("inf") else 0

if __name__ == '__main__':
    target = 11
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    print(solution.minSubArrayLen(target, nums))
