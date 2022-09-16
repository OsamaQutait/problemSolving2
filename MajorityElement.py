def majorityElement(nums):
    counter = {}
    size = int((len(nums) - 1) / 2)
    for num in nums:
        if counter.get(num) != None:
            counter[num] += 1
            if counter[num] >= size:
                return num
        else:
            counter[num] = 0
    return nums[0]


if __name__ == '__main__':
    print(majorityElement([1]))