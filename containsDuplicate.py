from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for num in nums:
            if num in nums_set:
                return True
            else:
                nums_set.add(num)
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.containsDuplicate([1, 2, 3, 1]))
