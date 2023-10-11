from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        arr_len = len(arr)
        ans = 0
        arr_sum = sum(arr[l:r+1])
        while r < arr_len:
            if (arr_sum / k) >= threshold:
                ans += 1
            l += 1
            r += 1
            if r < arr_len:
                arr_sum = arr_sum - arr[l-1] + arr[r]
        return ans


if __name__ == '__main__':
    arr = [2,2,2,2,5,5,5,8]
    k = 3
    threshold = 4
    solution = Solution()
    print(solution.numOfSubarrays(arr, k, threshold))