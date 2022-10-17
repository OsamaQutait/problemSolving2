import collections
def checkInclusion(s1: str, s2: str) -> bool:
    s1_dict = collections.UserDict()
    s2_dict = collections.UserDict()
    a_pointer, b_pointer = len(s1) - 1, 0
    for i in range(97, 123):
        s1_dict.__setitem__(chr(i), 0)
        s2_dict.__setitem__(chr(i), 0)
    for i in range(len(s1)):
        s1_dict.__setitem__(s1[i], s1_dict.__getitem__(s1[i]) + 1)
        s2_dict.__setitem__(s2[i], s2_dict.__getitem__(s2[i]) + 1)
    while True:
        try:
            if s2_dict == s1_dict:
                return True
            a_pointer += 1
            s2_dict.__setitem__(s2[a_pointer], s2_dict.__getitem__(s2[a_pointer]) + 1)
            s2_dict.__setitem__(s2[b_pointer], s2_dict.__getitem__(s2[b_pointer]) - 1)
            b_pointer += 1
        except IndexError:
            break
    return False
if __name__ == '__main__':
    print(checkInclusion("ab", "eidbaooo"))
    print(checkInclusion("abc", "bbbca"))