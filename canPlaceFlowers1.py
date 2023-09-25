from typing import List
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        flowerbed = [0] + flowerbed + [0]
        i = 1

        while i < len(flowerbed) - 1:
            if flowerbed[i - 1] == 0 and flowerbed[i] == 0 and flowerbed[i + 1] == 0:
                n -= 1
                i += 2
            else:
                i += 1

        return n <= 0


if __name__ == '__main__':
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 2
    solution = Solution()
    print(solution.canPlaceFlowers(flowerbed, n))