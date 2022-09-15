def sortedSquares(nums):
    len_nums = len(nums) - 1
    answer = [0]*(len_nums + 1)
    a_pointer, b_pointer, l_pointer = 0, len_nums, len_nums
    while l_pointer >= 0:
        if abs(nums[a_pointer]) > abs(nums[b_pointer]):
            answer[l_pointer] = nums[a_pointer] ** 2
            a_pointer += 1
            l_pointer -= 1
        else:
            answer[l_pointer] = nums[b_pointer] ** 2
            b_pointer -= 1
            l_pointer -= 1
    return answer

if __name__ == '__main__':
    print(sortedSquares([-7,-3,2,3,11]))
