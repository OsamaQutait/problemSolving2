from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        """
        Do not return anything, modify nums in-place instead.
        """

#
# from typing import *
# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         for i in range(k):
#             x = nums[-1]
#             nums.pop()
#             nums.insert(0, x)
#         """
#         Do not return anything, modify nums in-place instead.
#         """
if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5, 6, 7]
    #      [5, 6, 7, 1, 2, 3, 4]
    k = 3
    solution = Solution()
    print(solution.rotate(nums, k))