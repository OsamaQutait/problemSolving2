from typing import *
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0
if __name__ == '__main__':
    s = Solution
    print(s.canPlaceFlowers(None, [0,1,0], 1))