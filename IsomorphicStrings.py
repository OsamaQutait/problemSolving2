class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hash_map = {}
        ss = ""
        f1, f2 = True, True
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if not hash_map.__contains__(s[i]):
                hash_map.__setitem__(s[i], t[i])
            ss += hash_map.__getitem__(s[i])
        if ss != t:
            f1 = False
        hash_map = {}
        ss = ""
        for i in range(len(s)):
            if not hash_map.__contains__(t[i]):
                hash_map.__setitem__(t[i], s[i])
            ss += hash_map.__getitem__(t[i])
        if ss != s:
            f2 = False
        if not (f1 and f2):
            return False
        return True



if __name__ == '__main__':
    s = Solution
    print(s.isIsomorphic(None, "egg", "add"))