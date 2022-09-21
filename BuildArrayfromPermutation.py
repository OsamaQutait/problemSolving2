from typing import List
def buildArray(nums: List[int]) -> List[int]:
    size = len(nums) - 1
    answer = []
    for i in range(size + 1):
        answer.append(nums[nums[i]])
    return answer
if __name__ == '__main__':
    print(buildArray([5,0,1,2,3,4]))