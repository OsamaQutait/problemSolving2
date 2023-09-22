from typing import *
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, profit = 0, 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            else:
                profit = max(profit, prices[r] - prices[l])
        return profit

if __name__ == '__main__':
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))