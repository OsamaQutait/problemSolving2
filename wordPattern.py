class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_to_s = {}
        s_to_pattern = {}
        s = s.split(" ")
        if len(s) != len(pattern):
            return False
        for i in range(len(s)):
            if pattern[i] not in pattern_to_s:
                pattern_to_s[pattern[i]] = s[i]
            else:
                if pattern_to_s[pattern[i]] != s[i]:
                    return False
            if s[i] not in s_to_pattern:
                s_to_pattern[s[i]] = pattern[i]
            else:
                if s_to_pattern[s[i]] != pattern[i]:
                    return False

        return True

if __name__ == '__main__':
    pattern =  "aaaa"
    s = "dog cat cat dog"
    solution = Solution()
    print(solution.wordPattern(pattern, s))