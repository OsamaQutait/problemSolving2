print(ord('a'))
print(ord('z'))

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        num = list(map(int, input().split(" ")))
        print(sum(num) - (max(num)+min(num)))
