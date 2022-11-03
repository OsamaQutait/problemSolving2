def longestContinuousSubstring(s: str) -> int:
    sub_max_len = 1
    max_len = 1
    for i in range(1, len(s)):
        if ord(s[i])-ord(s[i-1])==1:
            sub_max_len += 1
        else:
            sub_max_len = 1
        max_len = max(max_len, sub_max_len)
    return max_len

if __name__ == '__main__':
    print(longestContinuousSubstring('yrpjofyzubfsiypfre'))
