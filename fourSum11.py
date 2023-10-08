from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        len_nums = len(nums)
        nums = sorted(nums)
        ans = []
        for index1, num1 in enumerate(nums):
            if index1 > 0 and nums[index1] == nums[index1 - 1]:
                continue
            for index2, num2 in enumerate(nums[index1 + 1:], start=index1 + 1):
                print(index2)
                if index2 > index1 + 1 and nums[index2] == nums[index2 - 1]:
                    continue
                l, r = index2 + 1, len_nums - 1
                while l < r:
                    nums_sum = nums[l] + nums[r] + num1 + num2
                    if nums_sum > target:
                        r -= 1
                    elif nums_sum < target:
                        l += 1
                    else:
                        ans.append([nums[l], nums[r], num1, num2])
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1
        return ans

if __name__ == '__main__':
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    solution = Solution()
    print(solution.fourSum(nums, target))
