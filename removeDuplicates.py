from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return len(sorted(set(nums)))

if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    solution = Solution()
    print(solution.removeDuplicates(nums))