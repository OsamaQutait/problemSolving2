if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        s = input()
        max_num = 97
        for char in s:
            max_num = max(max_num, ord(char))
        print(max_num - 98)
