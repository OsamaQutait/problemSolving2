def addDigits(num):
    if int(num / 10) == 0:
        return num
    sum = 0
    while num != 0:
        x = num % 10
        sum += x
        num //= 10
    return addDigits(sum)

if __name__ == '__main__':
    print(addDigits(0))

