def sortColors(nums):
    l_pointer = 0
    m_pointer = 0
    h_pointer = len(nums) - 1
    while m_pointer <= h_pointer:
        if nums[m_pointer] == 0:
            temp = nums[m_pointer]
            nums[m_pointer] = nums[l_pointer]
            nums[l_pointer] = temp
            m_pointer += 1
            l_pointer += 1
        elif nums[m_pointer] == 1:
            m_pointer += 1
        elif nums[m_pointer] == 2:
            temp = nums[m_pointer]
            nums[m_pointer] = nums[h_pointer]
            nums[h_pointer] = temp
            h_pointer -= 1
    return nums

if __name__ == "__main__":
    print(sortColors([2,0,1]))