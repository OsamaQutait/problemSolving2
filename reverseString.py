from typing import *
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
        print(s)
        """
        Do not return anything, modify s in-place instead.
        """

if __name__ == '__main__':
    s = ["H","a","n","n","a","h"]
    solution = Solution()
    print(solution.reverseString(s))