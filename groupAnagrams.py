from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_hash = {}
        for s in strs:
            t = ''.join(sorted(s))
            if t not in strs_hash:
                strs_hash[t] = [s]
            else:
                strs_hash[t].append(s)
        return list(strs_hash.values())


if __name__ == '__main__':
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    solution = Solution()
    print(solution.groupAnagrams(strs))
