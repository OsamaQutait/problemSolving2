from typing import *
def twoOutOfThree(nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    nums1, nums2, nums3 = set(nums1), set(nums2), set(nums3)
    answer = list(nums1.intersection(nums2).union(nums2.intersection(nums3)).union(nums1.intersection(nums3)))
    return answer

if __name__ == '__main__':
    print(twoOutOfThree([1, 1, 3, 2], [2, 3], [3]))