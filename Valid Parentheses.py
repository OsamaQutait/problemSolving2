def isValid(s: str) -> bool:
    s = [char for char in s]
    my_dict = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    i = len(s)-1
    while s:
        try:
            if my_dict.__getitem__(s[i]) == s[i-1]:
                s.pop()
                s.pop()
            else:
                return False
            i -= 2
        except IndexError:
            break
    return True

if __name__ == '__main__':
    print(isValid("()[]{}"))