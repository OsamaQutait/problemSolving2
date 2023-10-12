# class Solution:
#     def characterReplacement(self, s: str, k: int) -> int:
#         ans = 0
#         l, r = 0, 0
#         s_hash = {}
#         while r < len(s):
#             if s[r] in s_hash:
#                 s_hash[s[r]] += 1
#                 window_size = r-l+1
#                 if (window_size - max(s_hash.values())) <= k - 1:
#                     ans = max(ans, window_size)
#                 else:
#                     s_hash[s[l]] -= 1
#                     l += 1
#             else:
#                 s_hash[s[r]] = 1
#             r += 1
#         ans = max(ans, max(s_hash.values()))
#         return ans

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        l, r = 0, 0
        s_hash = {}
        max_count = 0
        while r < len(s):
            if s[r] in s_hash:
                s_hash[s[r]] += 1
            else:
                s_hash[s[r]] = 1
            max_count = max(max_count, s_hash[s[r]])
            if (r - l + 1 - max_count) > k:
                s_hash[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans


if __name__ == '__main__':
    s = "ABCDE"
    k = 1
    solution = Solution()
    print(solution.characterReplacement(s, k))