from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for num in nums:
            if num != val:
                ans.append(num)
        nums[:] = ans + [0] * (len(nums) - len(ans))
        return len(ans)

if __name__ == '__main__':
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    solution = Solution()
    new_length = solution.removeElement(nums, val)
    print(new_length)
    print(nums[:new_length])
