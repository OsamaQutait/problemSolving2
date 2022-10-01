from typing import *
def addToArrayForm(num: List[int], k: int) -> List[int]:
    answer = int("".join([str(n) for n in num]))
    answer += k
    return [int(n) for n in str(answer)]

if __name__ == '__main__':
    print(addToArrayForm([1, 2, 0, 0], 34))