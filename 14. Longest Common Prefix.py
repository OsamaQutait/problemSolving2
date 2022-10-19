from typing import *
def longestCommonPrefix(strs: List[str]) -> str:
    answer = ""
    two_d_array = []
    max_len = len(max(strs))
    for str in strs:
        row = [char for char in str]
        if len(row) != max_len:
            row.extend([""]*(max_len-len(row)))
        two_d_array.append(row)
    for j in range(max_len):
        flag = True
        for i in range(len(strs)):
            if two_d_array[i][j] != two_d_array[0][j]:
                flag = False
        if flag:
            answer += two_d_array[0][j]
        else:
            break
    return answer

if __name__ == '__main__':
    print(longestCommonPrefix(["a"]))