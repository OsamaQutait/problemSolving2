from typing import *
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        h = {}
        for index, num in enumerate(nums):
            if num in h and abs(index - h[num]) <= k:
                return True
            else:
                h[num] = index
        return False
if __name__ == '__main__':
    nums = [1,2,3,1,2,3]
    k = 2
    solution = Solution()
    print(solution.containsNearbyDuplicate(nums, k))