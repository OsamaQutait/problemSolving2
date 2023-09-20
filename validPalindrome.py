class Solution:
    def validPalindrome(self, s: str) -> bool:
        a_pointer = 0
        b_pointer = len(s)-1
        while b_pointer > a_pointer:
            if s[a_pointer] == s[b_pointer]:
                a_pointer += 1
                b_pointer -= 1
            else:
                s1 = s[:a_pointer] + s[a_pointer+1:]
                s2 = s[:b_pointer] + s[b_pointer+1:]
                return s1 == s1[::-1] or s2 == s2[::-1]
        return True

if __name__ == '__main__':
    s = "abc"
    solution = Solution()
    print(solution.validPalindrome(s))