from typing import *
def numSubarrayProductLessThanK(nums: List[int], k: int) -> int:
    counter, b_pointer, current_product = 0, 0, 1
    for a_pointer, num in enumerate(nums):
        current_product *= num
        while current_product >= k and a_pointer >= b_pointer:
            current_product //= nums[b_pointer]
            b_pointer += 1
        counter += a_pointer - b_pointer + 1
    return counter
if __name__ == '__main__':
    print(numSubarrayProductLessThanK([10,5,2,6], 100))
    print(numSubarrayProductLessThanK([10,2,2,5,4,4,4,3,7,7], 289))
