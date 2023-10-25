class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for str in s:
            if str != "*":
                stack.append(str)
            else:
                stack.pop()
        return "".join(stack)

if __name__ == '__main__':
    s = "leet**cod*e"
    solution = Solution()
    print(solution.removeStars(s))
