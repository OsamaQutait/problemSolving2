import collections
from typing import List
def majorityElement(nums: List[int]) -> List[int]:
    size = len(nums) // 3
    answer = []
    num = collections.Counter(n for n in nums)
    for item, amount in num.items():
        if amount > size:
            answer.append(item)
    return answer
if __name__ == '__main__':
    print(majorityElement([1, 2]))
