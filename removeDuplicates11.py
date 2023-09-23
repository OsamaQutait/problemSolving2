from typing import *
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        h = {}
        index, num = 0, 0
        while index < len(nums):
            num = nums[index]
            if num in h and h[num] >= 2:
                nums.pop(index)
            elif num in h and h[num] != 2:
                h[num] = h[num] + 1
                index += 1
            else:
                h[num] = 1
                index += 1
        print(nums)
        return len(nums)


if __name__ == '__main__':
    nums = [0,0,1,1,1,1,2,3,3]
    solution = Solution()
    print(solution.removeDuplicates(nums))
