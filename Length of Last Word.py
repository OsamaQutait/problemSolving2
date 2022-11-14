def lengthOfLastWord(s: str) -> int:
    caunter = 0
    s += ' '
    for i in reversed(range(len(s)-1)):
        if s[i] != ' ':
            caunter += 1
        if s[i] == ' ' and s[i + 1] != ' ':
            break
    return caunter

if __name__ == '__main__':
    print(lengthOfLastWord("Hello World"))
