import collections
def lengthOfLongestSubstring(s: str) -> int:
    max_len = 0
    max_sub_string = collections.OrderedDict()
    for char in s:
        if max_sub_string.__contains__(char):
            if char == list(max_sub_string)[0]:
                max_sub_string.popitem(last=False)
                max_sub_string.__setitem__(char, True)
                max_len = max(max_len, len(max_sub_string))
            else:
                while list(max_sub_string)[0] != char:
                    max_sub_string.popitem(last=False)
                max_sub_string.popitem(last=False)
                max_sub_string.__setitem__(char, True)
                max_len = max(max_len, len(max_sub_string))
        else:
            max_sub_string.__setitem__(char, True)
            max_len = max(max_len, len(max_sub_string))
    return max_len

if __name__ == '__main__':
    print(lengthOfLongestSubstring("ggububgvfk"))