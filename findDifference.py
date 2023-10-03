from typing import *
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        answer = [[], []]

        for num in nums1_set:
            if num not in nums2_set:
                answer[0].append(num)

        for num in nums2_set:
            if num not in nums1_set:
                answer[1].append(num)

        return answer

if __name__ == '__main__':
    nums1 = [1,2,3]
    nums2 = [2,4,6]
    solution = Solution()
    print(solution.findDifference(nums1, nums2))