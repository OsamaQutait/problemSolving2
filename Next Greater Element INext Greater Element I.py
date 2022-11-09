from typing import *
def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    nums1_dict = {num: i for i, num in enumerate(nums1)}
    stack = []
    answer = [-1] * len(nums1)
    for num in nums2:
        while stack and num > stack[-1]:
            answer[nums1_dict.__getitem__(stack[-1])] = num
            stack.pop()
        if nums1_dict.__contains__(num):
            stack.append(num)
    return answer

if __name__ == '__main__':
    print(nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
