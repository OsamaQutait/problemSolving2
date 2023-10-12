class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}
        s2_hash = {}
        for char in 'abcdefghijklmnopqrstuvwxyz':
            s1_hash[char] = 0
            s2_hash[char] = 0
        for char in s1:
            s1_hash[char] += 1

        l, r = 0, 0
        while r < len(s2):
            s2_hash[s2[r]] += 1
            if r - l + 1 == len(s1):
                matches = 0
                for char in s1_hash.keys():
                    if s1_hash[char] == s2_hash[char]:
                        matches += 1

                if matches == 26:
                    return True

                s2_hash[s2[l]] -= 1
                l += 1

            r += 1

        return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    solution = Solution()
    print(solution.checkInclusion(s1, s2))
