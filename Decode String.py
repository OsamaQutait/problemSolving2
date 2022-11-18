def decodeString(s: str) -> str:
    stack = []
    num = ''
    sub_string = ''
    for char in s:
        if char != ']':
            stack.append(char)
        else:
            while stack[-1] != '[':
                sub_string = stack.pop() + sub_string
            stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            stack.append(sub_string*int(num))
            sub_string = ''
            num = ''
    print(stack)
    return ''.join(stack)

if __name__ == '__main__':
    print(decodeString("3[a]2[bc]"))