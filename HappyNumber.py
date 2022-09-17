def isHappy(n):
    sum = 0
    if n == 1:
        return True
    if n < 7 and n > 1:
        return False
    while n != 0:
        x = n % 10
        sum += x**2
        n = int(n / 10)
    return isHappy(sum)


if __name__ == '__main__':
    print(isHappy(2))