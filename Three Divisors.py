import math
def isThree(n: int) -> bool:
    if n == 1 or n == 2:
        return False
    if int(math.sqrt(n)) ** 2 != n:
        return False
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False



if __name__ == '__main__':
    print(isThree(4))