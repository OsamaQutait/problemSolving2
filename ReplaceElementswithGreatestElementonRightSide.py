from typing import List
def replaceElements(arr: List[int]) -> List[int]:
    right_pointer = len(arr) - 1
    answer = [0] * (right_pointer + 1)
    max_num = -1
    if len(arr) == 1:
        return [-1]
    else:
        for i in reversed(range(right_pointer + 1)):
            try:
                answer[i - 1] = max(max_num, arr[i])
                max_num = answer[i - 1]
            except IndexError:
                break
        answer[right_pointer] = -1
        return answer


def test_replaceElements():
    arr = [17,18,5,4,6,1]
    answer = [18,6,6,6,1,-1]
    assert replaceElements(arr) == answer
# if __name__ == '__main__':
#     arr = [17, 18, 5, 4, 6, 1]
#     print(replaceElements(arr))