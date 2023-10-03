from typing import *
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        product = 1
        for num in nums:
            product *= num
        if product == 0:
            return 0
        elif product >= 1:
            return 1
        else:
            return -1

if __name__ == '__main__':
    nums = [1,5,0,2,-3]
    solution = Solution()
    print(solution.arraySign(nums))