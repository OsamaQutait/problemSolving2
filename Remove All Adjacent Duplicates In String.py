# def removeDuplicates(s: str) -> str:
#     i = 0
#     while True:
#         try:
#             if s[i] == s[i+1]:
#                 s = s.replace(s[i:i+2], '', 1)
#                 if i >= 1:
#                     i = i-1
#             else:
#                 i += 1
#         except IndexError:
#             break
#     return s

def removeDuplicates(s: str) -> str:
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

if __name__ == '__main__':
    print(removeDuplicates("aababaab"))