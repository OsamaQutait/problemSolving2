from typing import *
def reverseString(s: List[str]) -> None:
    left_pointer, right_pointer = 0, len(s) - 1
    while left_pointer <= right_pointer:
        s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
        left_pointer += 1
        right_pointer -= 1

if __name__ == '__main__':
    reverseString(["H","a","n","n","a","h"])