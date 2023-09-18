from typing import *
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hash = {}
        for index, num in enumerate(nums):
            if num_hash.__contains__(target-num):
                return [index, num_hash.__getitem__(target-num)]
            else:
                num_hash.__setitem__(num, index)

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    solution = Solution()
    print(solution.twoSum(nums, target))