class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for s in path:
            if s == "..":
                if stack:
                    stack.pop()
            elif s != '' and s != '/' and s != '.':
                stack.append(s)
        return '/' + '/'.join(stack)


if __name__ == '__main__':
    s = Solution
    print(s.simplifyPath(None, "/../abc//./def/"))
