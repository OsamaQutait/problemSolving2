from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        l = 0
        r = len(nums) - 1
        while r > l:
            ans.append(nums[l])
            ans.append(nums[r])
            l += 1
            r -= 1
        if l == r:
            ans.append(nums[l])
        return ans




if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    solution = Solution()
    print(solution.rearrangeArray(nums))