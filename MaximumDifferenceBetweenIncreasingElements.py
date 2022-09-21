from typing import *
def maximumDifference(nums: List[int]) -> int:
    min = nums[0]
    answer = -1
    for i in nums:
        if i > min:
            answer = max(answer, i - min)
        else:
            min = i
    return answer
if __name__ == '__main__':
    print(maximumDifference([7,1,5,4]))