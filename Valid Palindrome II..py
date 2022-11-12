def validPalindrome(s: str) -> bool:
    def is_valid_palindrome(s: str) -> bool:
        l, r = 0, len(s) - 1
        while r >= l:
            if s[r] == s[l]:
                l += 1
                r -= 1
            else:
                return False
        return True
    l, r = 0, len(s)-1
    while r >= l:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            s1 = s[:l] + "" + s[l+1:]
            s2 = s[:r] + "" + s[r+1:]
            return is_valid_palindrome(s1) or is_valid_palindrome(s2)
    return True

if __name__ == '__main__':
    # print(validPalindrome("abac"))
    print(validPalindrome("cbbcc"))