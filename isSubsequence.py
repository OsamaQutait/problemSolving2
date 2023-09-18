class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        a_pointer, s_len = 0, len(s)
        if s_len == 0 or s_len > len(t):
            return False
        for char in t:
            if char == s[a_pointer]:
                a_pointer += 1
            if a_pointer == s_len:
                return True
        return False

if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"
    solution = Solution()
    print(solution.isSubsequence(s, t))
