import collections
from typing import *
def findMin(nums: List[int]) -> int:
    my_dict = collections.Counter(nums)
    return sorted(my_dict.keys())[0]
if __name__ == '__main__':
    print(findMin([2, 2, 2, 0, 1]))
    print(findMin([1,3,5]))