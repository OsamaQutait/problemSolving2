from typing import *
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area, l, r = 0, 0, len(height) - 1
        while r > l:
            area = max(area, min(height[l], height[r])*(r-l))
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return area


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    solution = Solution()
    print(solution.maxArea(height))