import collections
def characterReplacement(s: str, k: int) -> int:
    max_len, a_pointer, b_pointer, max_freq_char = 0, 0, 0, 0
    sub_string = collections.UserDict()
    while a_pointer < len(s):
        current_len = a_pointer - b_pointer + 1
        if sub_string.__contains__(s[a_pointer]):
            sub_string.__setitem__(s[a_pointer], sub_string.__getitem__(s[a_pointer])+1)
        else:
            sub_string.__setitem__(s[a_pointer], 1)
        max_freq_char = max(max_freq_char, sub_string.__getitem__(s[a_pointer]))
        if abs(current_len - max_freq_char) <= k:
            max_len = max(max_len, current_len)
        else:
            sub_string.__setitem__(s[b_pointer], sub_string.__getitem__(s[b_pointer])-1)
            if sub_string.__getitem__(s[b_pointer]) == 0:
                sub_string.pop(s[b_pointer])
            b_pointer += 1
        a_pointer += 1
    return max_len
if __name__ == '__main__':
    print(characterReplacement("ABAA", 0))