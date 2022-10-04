def validPalindrome(s: str) -> bool:
    leftPointer, counter, rightPointer = 0, 0, len(s) - 1
    while rightPointer >= leftPointer:
        if rightPointer == leftPointer:
            break
        if s[rightPointer] == s[leftPointer]:
            leftPointer += 1
            rightPointer -= 1
        else:
            if not counter:
                leftPointer += 1
                counter += 1
            else:
                return False
    if counter == 1 or counter == 0:
        return True
    leftPointer, counter, rightPointer = 0, 0, len(s) - 1
    while rightPointer >= leftPointer:
        if rightPointer == leftPointer:
            break
        if s[rightPointer] == s[leftPointer]:
            leftPointer += 1
            rightPointer -= 1
        else:
            if not counter:
                rightPointer -= 1
                counter += 1
            else:
                return False
    if counter == 1 or counter == 0:
        return True

if __name__ == '__main__':
    print(validPalindrome("cbbcc"))