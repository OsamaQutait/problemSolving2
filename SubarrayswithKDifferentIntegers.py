from typing import *
import collections

def subarraysWithKDistinct(nums: List[int], k: int) -> int:
    def atMostK(nums: List[int], k: int) -> int:
        sub_string = collections.UserDict()
        b_pointer, counter, a_pointer = 0, 0, 0
        while a_pointer < len(nums):
            if sub_string.__contains__(nums[a_pointer]):
                sub_string.__setitem__(nums[a_pointer], sub_string.__getitem__(nums[a_pointer]) + 1)
            else:
                sub_string.__setitem__(nums[a_pointer], 1)
            while len(sub_string) > k:
                sub_string.__setitem__(nums[b_pointer], sub_string.__getitem__(nums[b_pointer]) - 1)
                if sub_string.__getitem__(nums[b_pointer]) == 0:
                    sub_string.pop(nums[b_pointer])
                b_pointer += 1
            counter += a_pointer - b_pointer + 1
            a_pointer += 1
        return counter
    return atMostK(nums, k) - atMostK(nums, k-1)

if __name__ == '__main__':
    print(subarraysWithKDistinct([2,1,1,1,2], 1))
    # print(atMostK([1, 2, 1, 2, 3], 1))
    # print(atMostK([1, 2, 1, 2, 3], 2))
    # print(atMostK([1, 2, 1, 3, 4], 3))
    # print(atMostK([1, 2, 1, 3, 4], 2))