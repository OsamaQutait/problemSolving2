import collections
def repeatedSubstringPattern(s: str) -> bool:
    if len(s) == 1:
        return False
    s_dict = collections.Counter(s)
    if len(s_dict) == 1:
        return True
    a_pointer, b_pointer = 1, 0
    while a_pointer < len(s) + 1:
        factor = len(s) / (a_pointer - b_pointer + 1)
        if factor.is_integer():
            if s[b_pointer:a_pointer + 1] * int(factor) == s and int(factor) != 1:
                return True
        a_pointer += 1
    return False
if __name__ == '__main__':
    print(repeatedSubstringPattern("bb"))