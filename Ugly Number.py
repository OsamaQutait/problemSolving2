def isUgly(n):
    for i in [2, 3, 5]:
        while n % i == 0:
            n /= i
    return n == 1

if __name__ == '__main__':
    print(isUgly(14))