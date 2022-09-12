def findDuplicate(nums):
    my_hash = {}
    for num in nums:
        if my_hash.get(num):
            return num
        else:
            my_hash[num] = True



if __name__ == '__main__':
    print(findDuplicate([3,1,3,4,2]))
