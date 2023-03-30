class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i <= len(path)-1:
            # if len(stack) >= 2:
            if path[i] + path[i+1] == "..":
                if len(stack) >= 2:
                    stack.pop()
            elif (path[i] == "/" and path[i+1] != "/") or path[i] + path[i+1] == "//" :
                stack.append('/')
            elif path[i] != "." and path[i] != "/":
                s = ""
                while path[i] != "." and path[i] != "/":
                    s += path[i]
                    i += 1
                stack.append(s)
            i += 1
        return ''.join(stack)


if __name__ == '__main__':
    s = Solution
    print(s.simplifyPath(None, "/../abc//./def/"))