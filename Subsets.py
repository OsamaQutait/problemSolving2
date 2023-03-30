from typing import *
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        subset = []

        def dfs(num: int):
            if num >= len(nums):
                ans.append(subset.copy())
                return
            subset.append(nums[num])
            dfs(num+1)
            subset.pop()
            dfs(num + 1)
        dfs(0)
        return ans



if __name__ == '__main__':
    s = Solution
    print(s.subsets(None, [1, 2, 3]))