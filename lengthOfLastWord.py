class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        return len(s[len(s) - 1])


if __name__ == '__main__':
    s = "   fly me   to   the moon  "
    solution = Solution()
    print(solution.lengthOfLastWord(s))