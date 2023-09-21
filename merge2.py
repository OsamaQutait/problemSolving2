from typing import *
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a_pointer, b_pointer, c_pointer = m-1, n-1, len(nums1)-1
        while b_pointer != -1 and a_pointer != -1:
            if nums1[a_pointer] > nums2[b_pointer]:
                nums1[c_pointer] = nums1[a_pointer]
                a_pointer -= 1
                c_pointer -= 1
            else:
                nums1[c_pointer] = nums2[b_pointer]
                b_pointer -= 1
                c_pointer -= 1
        while b_pointer != -1:
            nums1[c_pointer] = nums2[b_pointer]
            b_pointer -= 1
            c_pointer -= 1
        print(nums1)


if __name__ == '__main__':
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution = Solution()
    print(solution.merge(nums1, m, nums2, n))