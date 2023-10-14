class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels_set = {'a', 'e', 'i', 'o', 'u'}
        ans = 0
        count = 0
        l, r = 0, 0

        while r < k:
            if s[r] in vowels_set:
                ans += 1
            r += 1

        count = ans

        while r < len(s):
            if s[r] in vowels_set:
                ans += 1
            if s[l] in vowels_set:
                ans -= 1
            r += 1
            l += 1
            count = max(ans, count)

        return count



if __name__ == '__main__':
    s = "ibpbhixfiouhdljnjfflpapptrxgcomvnb"
    k = 33
    solution = Solution()
    print(solution.maxVowels(s, k))
