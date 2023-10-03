class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l, r = 0, len(needle)-1
        while r < len(haystack):
            if haystack[l: r+1] == needle:
                return l
            else:
                l += 1
                r += 1
        return -1


if __name__ == '__main__':
    haystack = "sadbutsad"
    needle = "sad"
    solution = Solution()
    print(solution.strStr(haystack, needle))