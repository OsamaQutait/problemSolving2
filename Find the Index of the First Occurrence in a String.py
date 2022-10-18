import collections
def strStr(haystack: str, needle: str) -> int:
    a_pointer, b_pointer, index = len(needle) - 1, 0, 0
    while a_pointer < len(haystack):
        if needle == haystack[b_pointer:a_pointer + 1]:
            return b_pointer
        else:
            a_pointer += 1
            b_pointer += 1
    return -1

if __name__ == '__main__':
    print(strStr("sadbutsad", "sad"))