from typing import *
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        for i in range(0, numRows+1):
            helper = [1]*i
            if i >= 3:
                for j in range(0, i-2):
                    helper[j+1] = ans[i-1][j] + ans[i-1][j+1]
                ans.append(helper)
            else:
                ans.append(helper)
        return ans

if __name__ == '__main__':
    numRows = 5
    solution = Solution()
    print(solution.generate(numRows))



