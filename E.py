if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(n):
        num = list(map(int, input().split(" ")))
        nums.append(num)

    for x in nums:
        score = []
        for j in x:
            
