from typing import *
import collections
def subarraySum(nums: List[int], k: int) -> int:
    counter, currint_sum = 0, 0
    prefix_sum = collections.UserDict()
    for num in nums:
        currint_sum += num
        if currint_sum == k:
            counter += 1
        val = currint_sum - k
        if prefix_sum.__contains__(val):
            counter += prefix_sum.__getitem__(val)
        if prefix_sum.__contains__(currint_sum):
            prefix_sum.__setitem__(currint_sum, prefix_sum.__getitem__(currint_sum)+1)
        else:
            prefix_sum.__setitem__(currint_sum, 1)
    return counter

def count_sub_array(nums):
    counter = 0
    for a_pointer, num in enumerate(nums):
        counter += a_pointer + 1
    return counter

if __name__ == '__main__':
    # print(subarraySum([1, 1, 1], 2))
    # print(subarraySum([1, 2, 3], 3))
    # print(subarraySum([1], 0))
    # print(subarraySum([-1,-1,1], 0))
    print(subarraySum([0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0))
    # print(count_sub_array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
