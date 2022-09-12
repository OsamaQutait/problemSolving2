def findDuplicates(nums):
    unique = {}
    duplicates = []
    for num in nums:
        if unique.get(num):
            unique[num] += 1
            duplicates.append(num)
        else:
            unique[num] = 1
    return duplicates

if __name__ == "__main__":
    print(findDuplicates([1]))