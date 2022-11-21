if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = input()
        nums = list(map(int, input().split(" ")))
        nums1 = nums.copy()
        answer = []
        nums1.sort()
        for num in nums:
            if num == nums1[-1]:
                answer.append(str(num-nums1[-2]))
            else:
                answer.append(str(num-nums1[-1]))
        print(" ".join(answer))
