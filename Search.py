def search(nums, target):
    start = 0
    end = len(nums) - 1
    while end >= start:
        mid = int((start + end) / 2)
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        elif nums[mid] == target:
            return mid
    return -1

if __name__ == '__main__':
    print(search([5], 5))
