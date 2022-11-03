import collections
def minWindow(s: str, t: str) -> str:
    s_dict = collections.UserDict()
    t_dict = collections.UserDict()
    answer = [0, len(s)]
    have, need, left_pointer, right_pointer = 0, 0, 0, 0
    for i in range(65, 91):
        s_dict.__setitem__(chr(i), 0)
        t_dict.__setitem__(chr(i), 0)
    for char in t:
        t_dict.__setitem__(char, t_dict.__getitem__(char) + 1)
    have = sum(1 for num in list(t_dict.values()) if num > 0)

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(minWindow(s, t))
