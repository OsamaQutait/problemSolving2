def findDisappearedNumbers(nums):
    unique = {}
    result = []
    for num in nums:
        unique[num] = True
    for number in range(1, len(nums)+1):
        if unique.get(number):
            continue
        else:
            result.append(number)
    return result

if __name__ == "__main__":
    print(findDisappearedNumbers([1,1]))