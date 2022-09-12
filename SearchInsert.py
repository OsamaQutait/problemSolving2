def searchInsert(nums, target):
    l_pointer = 0
    r_pointer = len(nums) - 1
    if target > nums[len(nums) - 1]:
        return len(nums)
    while r_pointer >= l_pointer:
        m_pointer = int((r_pointer + l_pointer) // 2)
        if nums[m_pointer] == target:
            return m_pointer
        if nums[m_pointer] < target:
            l_pointer = m_pointer + 1
        else:
            r_pointer = m_pointer - 1
    return l_pointer

if __name__ == '__main__':
    print(searchInsert([1,3,5], 4))