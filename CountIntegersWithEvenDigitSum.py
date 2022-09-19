def countEven(num: int) -> int:
    counter = 0
    for n in range(2, num+1):
        sum = 0
        while n != 0:
            sum += n % 10
            n //= 10
        if (sum % 2) == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    print(countEven(30))
