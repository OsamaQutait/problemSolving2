class Solution:
    def nextGreaterElement(self, n: int) -> int:
        n = str(n)
        arr = [i for i in n]
        if len(arr) == 1:
            return -1

        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        if i < 0:
            return -1
        j = len(arr) - 1
        while arr[i] >= arr[j]:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = reversed(arr[i+1:])
        ans = ''.join(arr)
        return int(ans) if int(ans) < 2**31 else -1


if __name__ == '__main__':
    s = Solution
    print(s.nextGreaterElement(None, 23102431))