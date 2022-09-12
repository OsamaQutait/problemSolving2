def moveZeroes(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r]:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
    return nums

if __name__ == '__main__':
    print(moveZeroes([6, 5, 8, 0, 0,9]))