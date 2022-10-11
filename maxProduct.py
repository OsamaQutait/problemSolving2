from typing import *
def maxProduct(nums: List[int]) -> int:
    maxProd, minProd, answer = 1, 1, nums[0]
    for num in nums:
        value = (num, maxProd*num, minProd*num)
        maxProd, minProd = max(value), min(value)
        answer = max(answer, maxProd)
    return answer

if __name__ == '__main__':
    print(maxProduct([2,3,-2,4]))
