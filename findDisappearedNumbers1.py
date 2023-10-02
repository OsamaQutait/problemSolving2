from typing import *
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        nums, ans = set(sorted(nums)), []
        for i in range(1, len_nums+1):
            if i not in nums:
                ans.append(i)
        return ans

if __name__ == '__main__':
    nums = [1,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(nums))