from typing import *
def maxDistance(colors: List[int]) -> int:
    left_pointer = 0
    right_pointer = len(colors) - 1
    while colors[left_pointer] == colors[right_pointer]:
        right_pointer -= 1
    answer1 = right_pointer - left_pointer
    while colors[left_pointer] == colors[len(colors) - 1]:
        left_pointer += 1
    answer2 = len(colors) - 1 - left_pointer
    return max(answer2, answer1)

def test_maxDistance():
    colors = [4,4,4,11,4,4,11,4,4,4,4,4]
    assert maxDistance(colors) == 8

