from typing import *
def sortByBits(arr: List[int]) -> List[int]:
    answer = sorted([(bin(num).count("1"), num) for num in arr])
    return [num[1] for num in answer]

if __name__ == '__main__':
    print(sortByBits( [1024,512,256,128,64,32,16,8,4,2,1]))