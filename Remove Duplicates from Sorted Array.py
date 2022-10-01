from typing import *
def removeDuplicates(nums: List[int]) -> int:
    a_pointer, b_pointer = 0, 1
    while True:
        try:
            if nums[a_pointer] != nums[b_pointer]:
                a_pointer += 1
                b_pointer += 1
                continue
            else:
                nums.remove(nums[a_pointer])
        except IndexError:
            break
    return len(nums)

if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))