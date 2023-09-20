class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        for i in range(min(len(word2), len(word1))):
            ans += word1[i] + word2[i]
        if len(word2) > len(word1):
            ans += word2[len(word1):]
        elif len(word2) < len(word1):
            ans += word1[len(word2):]
        return ans

if __name__ == '__main__':
    word1 = "abcd"
    word2 = "pq"
    solution = Solution()
    print(solution.mergeAlternately(word1, word2))