from typing import *
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        num1_set = set(nums1)
        num2_h = {}
        max_num = 0
        for i in range(len(nums2)):
            flag = True
            if i == len(nums2)-1:
                max_num = -1
            else:
                for j in range(i+1, len(nums2)):
                    if nums2[j] > nums2[i]:
                        max_num = nums2[j]
                        flag = False
                        break
                if flag:
                    max_num = -1
            num2_h[nums2[i]] = max_num
        for num in nums1:
            ans.append(num2_h[num])
        return ans

if __name__ == '__main__':
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    solution = Solution()
    print(solution.nextGreaterElement(nums1, nums2))