def reverseStr(s: str, k: int) -> str:
    for i in range(0, len(s), 2 * k):
        if (i + k < len(s)):
            s = s[0:i] + s[i:i + k][::-1] + s[i + k:]
        else:
            s = s[0:i] + s[i:i + k][::-1]
    return s

if __name__ == '__main__':
    print(66)
