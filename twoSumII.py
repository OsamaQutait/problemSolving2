from typing import *
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l != r:
            if numbers[l] + numbers[r] > target:
                r -= 1
            elif numbers[l] + numbers[r] < target:
                l += 1
            else:
                return [l+1, r+1]

if __name__ == '__main__':
    numbers = [2, 7, 11, 15]
    target = 9
    solution = Solution()
    print(solution.twoSum(numbers, target))