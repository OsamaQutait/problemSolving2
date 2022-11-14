from typing import *
def removeDuplicates(nums: List[int]) -> int:
    caunter = 0
    my_dict = {}
    for num in nums:
        if my_dict.__contains__(num):
            my_dict[num] += 1
        else:
            my_dict.__setitem__(num, 0)
            caunter += 1
    return caunter

if __name__ == '__main__':
    print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))