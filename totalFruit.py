from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, r = 0, 0
        fruits_set = {}
        ans = 0
        while r < len(fruits):
            if fruits[r] in fruits_set:
                fruits_set[fruits[r]] += 1
            else:
                fruits_set[fruits[r]] = 1
                while len(fruits_set) > 2:
                    fruits_set[fruits[l]] -= 1
                    if fruits_set[fruits[l]] == 0:
                        del fruits_set[fruits[l]]
                    l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans

if __name__ == '__main__':
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    solution = Solution()
    print(solution.totalFruit(fruits))
