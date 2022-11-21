if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        nums = list(map(int, input().split(" ")))
        nums1 = nums.copy()
        for j in range(n-1):
            if nums[j] == 0:
                nums[j] = 1
                break
        ones_counter = 0
        maximum_inversions = 0
        for num in nums:
            if num == 1:
                ones_counter += 1
            else:
                maximum_inversions += ones_counter

        for i in reversed(range(n)):
            if nums1[i] == 1:
                nums1[i] = 0
                break
        ones_counter1 = 0
        maximum_inversions1 = 0
        for num in nums1:
            if num == 1:
                ones_counter1 += 1
            else:
                maximum_inversions1 += ones_counter1

        print(max(maximum_inversions, maximum_inversions1))


