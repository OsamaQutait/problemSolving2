from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        len_nums = len(nums)
        nums = sorted(nums)
        ans = []
        for index, num in enumerate(nums):
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            l, r = index + 1, len_nums - 1
            while l < r:
                nums_sum = nums[l] + nums[r] + num
                if nums_sum > 0:
                    r -= 1
                elif nums_sum < 0:
                    l += 1
                else:
                    ans.append([nums[l], nums[r], num])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans

if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    solution = Solution()
    print(solution.threeSum(nums))
