def removeElement(nums, val):
    while True:
        try:
            nums.remove(val)
        except ValueError:
            break
    return len(nums)

if __name__ == '__main__':
    print(removeElement([3, 2, 2, 3], 3))
