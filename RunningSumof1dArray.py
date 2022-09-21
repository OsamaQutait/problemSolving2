from typing import List
def runningSum(nums: List[int]) -> List[int]:
    answer = []
    sum = 0
    for num in nums:
        sum += num
        answer.append(sum)
    return answer
if __name__ == '__main__':
    print(runningSum([3,1,2,10,1]))