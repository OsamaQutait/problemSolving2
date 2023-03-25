from typing import *
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * (len(nums))
        n = len(nums)
        stack = []
        for i in range(n*2):
            while stack and nums[i % n] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return ans

if __name__ == '__main__':
    s = Solution
    print(s.nextGreaterElements(None, [1,3,4,2]))