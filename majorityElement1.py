from typing import *
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1
        for key, value in h.items():
            if key/2 < value:
                return key

if __name__ == '__main__':
    nums = [4,5,4]
    solution = Solution()
    print(solution.majorityElement(nums))