def isSubsequence(s: str, t: str) -> bool:
    j = 0
    for i in range(len(t)):
        if j > len(s)-1:
            break
        if s and t[i] == s[j]:
            j += 1
    return True if len(s) == j else False

if __name__ == '__main__':
    print(isSubsequence("", "abc"))
