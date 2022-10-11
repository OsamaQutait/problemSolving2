def pivotIndex(nums):
    a_pointer = 0
    l_sum = 0
    total_sum = sum(nums)
    while a_pointer <= (len(nums) - 1):
        r_sum = total_sum - l_sum - nums[a_pointer]
        if l_sum == r_sum:
            return a_pointer
        l_sum += nums[a_pointer]
        a_pointer += 1
    return -1

if __name__ == '__main__':
    # print(pivotIndex([8,3,7,2,1,1]))
    # print(pivotIndex([1,7,3,6,5,6]))
    print(pivotIndex([6,9,1,4,10,6]))
