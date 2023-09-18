from typing import *
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = []
        arr_len = len(arr) - 1
        max_num = max(arr)
        for a_pointer, num in enumerate(arr):
            if arr_len == a_pointer:
                break
            if max_num == num:
                max_num = max(arr[a_pointer+1:])
                ans.append(max_num)
            if max_num > num:
                ans.append(max_num)

        ans.append(-1)
        return ans

if __name__ == '__main__':
    s = Solution()
    print(s.replaceElements([17]))