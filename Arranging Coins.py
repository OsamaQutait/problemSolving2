def arrangeCoins(n: int) -> int:
    l, r = 0, n
    answer = 0
    if n == 1:
        return 1
    while r >= l:
        mid = (l + r) // 2
        if ((mid / 2)*(mid + 1)) > n:
            r = mid - 1
        else:
            l = mid + 1
            answer = max(mid, answer)
    return answer
if __name__ == '__main__':
    print(arrangeCoins(8))