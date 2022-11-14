from typing import *
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    my_dict = {}
    answer = []
    for str in strs:
        temp = str
        str = "".join(sorted(str))
        if my_dict.__contains__(str):
            my_dict.__setitem__(str, my_dict.__getitem__(str)+' '+temp)
        else:
            my_dict.__setitem__(str, temp)
    for key, value in my_dict.items():
        answer.append(value.split(' '))
    return answer


if __name__ == '__main__':
    groupAnagrams(["eat","tea","tan","ate","nat","bat"])