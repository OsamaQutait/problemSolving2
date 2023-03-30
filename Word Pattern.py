class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hash_map1 = {}
        hash_map2 = {}
        for i in range(len(s)):
            if not hash_map1.__contains__(pattern[i]):
                hash_map1.__setitem__(pattern[i], s[i])
            elif hash_map1.__getitem__(pattern[i]) != s[i]:
                return False
            if not hash_map2.__contains__(s[i]):
                hash_map2.__setitem__(s[i], pattern[i])
            elif hash_map2.__getitem__(s[i]) != pattern[i]:
                return False
        return True

if __name__ == '__main__':
    s = Solution
    print(s.wordPattern(None, "abba", "dog dog dog dog"))