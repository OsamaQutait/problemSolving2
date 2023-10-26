class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() +substr
                stack.pop()
                digit = ""
                while stack and stack[-1].isdigit():
                    digit = stack.pop() + digit
                stack.append(int(digit)*(substr))
        return "".join(stack)

if __name__ == '__main__':
    s = "3[a]2[bc]"
    solution = Solution()
    print(solution.decodeString(s))

    s = "3[a2[c]]"
    print(solution.decodeString(s))

    s = "2[abc]3[cd]ef"
    print(solution.decodeString(s))
