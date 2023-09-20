import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-z A-Z]', '', s.replace(" ", "")).lower()
        a_pointer, b_pointer = 0, len(s)-1
        if not len(s):
            return True
        while a_pointer < b_pointer:
            if s[a_pointer] == s[b_pointer]:
                a_pointer += 1
                b_pointer -= 1
            else:
                return False
        return True

if __name__ == '__main__':
    s = "dd"
    solution = Solution()
    print(solution.isPalindrome(s))
