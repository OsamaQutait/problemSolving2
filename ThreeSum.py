def threeSum(nums):
    nums = sorted(nums)
    result = []
    for i in range(len(nums)):
        if nums[i] == nums[i - 1] and i > 0:
            continue
        a_pointer = i + 1
        b_pointer = len(nums) - 1
        while b_pointer > a_pointer and len(nums) > b_pointer:
            if sum([nums[i], nums[a_pointer], nums[b_pointer]]) > 0:
                b_pointer -= 1
            elif sum([nums[i], nums[a_pointer], nums[b_pointer]]) < 0:
                a_pointer += 1
            else:
                result.append([nums[i], nums[a_pointer], nums[b_pointer]])
                a_pointer += 1
                while nums[a_pointer] == nums[a_pointer - 1] and a_pointer < b_pointer and \
                        a_pointer <= len(nums) - 1 and b_pointer <= len(nums) - 1:
                    a_pointer += 1
    return result

if __name__ == '__main__':
    print(threeSum([0,0,0]))
