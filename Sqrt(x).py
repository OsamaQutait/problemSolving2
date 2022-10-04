def mySqrt(x: int) -> int:
    leftPointer, rightPointer = 0, x
    while rightPointer > leftPointer:
        mid = leftPointer + (rightPointer - leftPointer) / 2
        if round(mid**2, 1) == x:
            return int(mid)
        if mid**2 > x:
            rightPointer = mid
        else:
            leftPointer = mid
    if rightPointer**2 == x:
        return int(rightPointer)
    return 0
if __name__ == "__main__":
    print(mySqrt(9))
