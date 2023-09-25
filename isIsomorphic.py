class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        h = {}
        a = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in h:
                if h[s[i]] != t[i]:
                    return False
            else:
                h[s[i]] = t[i]

            if t[i] in a:
                if a[t[i]] != s[i]:
                    return False
            else:
                a[t[i]] = s[i]
        return True

if __name__ == '__main__':
    s = "foo"
    t = "bar"
    solution = Solution()
    print(solution.isIsomorphic(s, t))