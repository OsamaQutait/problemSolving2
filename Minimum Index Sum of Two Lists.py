from typing import *
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        l1 = set(list1)
        l2 = set(list2)
        my_hash = {}
        group = l1.intersection(l2)
        for i, s in enumerate(list1):
            if group.__contains__(s):
                my_hash[s] = i
        for i, s in enumerate(list2):
            if group.__contains__(s):
                my_hash.__setitem__(s, my_hash.__getitem__(s)+i)
        ans = []
        my_hash = sorted(my_hash.items(), key=lambda x:x[1])
        minSum = my_hash[0][1]
        for i in my_hash:
            if i[1] == minSum:
                ans.append(i[0])
            else:
                break
        return ans

if __name__ == '__main__':
    list1 = ["Shogun", "osama", "Burger King", "KFC"]
    list2 = ["Piatti", "osama", "ooo", "Shogun"]
    s = Solution()
    print(s.findRestaurant(list1, list2))