class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        ans = 0
        l, r = 0, 0
        while r < len(s):
            if s[r] not in s_set:
                s_set.add(s[r])
                ans = max(ans, len(s_set))
                r += 1
            else:
                while s[r] in s_set:
                    s_set.remove(s[l])
                    l += 1
        return ans

if __name__ == '__main__':
    s = "dvdf"
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s))