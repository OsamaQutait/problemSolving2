import re
def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub(r'[^a-z0-9]+', '', s)
    leftPointer, rightPointer = 0, len(s) - 1
    while rightPointer >= leftPointer:
        if s[rightPointer] == s[leftPointer]:
            leftPointer += 1
            rightPointer -= 1
        else:
            return False
    return True

if __name__ == '__main__':
    print(isPalindrome("A man, a plan, a canal: Panama"))