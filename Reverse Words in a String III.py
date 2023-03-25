class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        for i in range(len(s)):
            s[i] = s[i][::-1]
        s = " ".join(s)
        return s

if __name__ == '__main__':
    s = Solution
    print(s.reverseWords(None, "Let's take LeetCode contest"))