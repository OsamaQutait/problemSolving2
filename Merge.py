def merge(nums1, m, nums2, n):
    answer = []
    a_pointer = 0
    b_pointer = 0
    while a_pointer < len(nums1) and b_pointer < len(nums2):
        if nums1[a_pointer] > nums2[b_pointer]:
            answer.append(nums2[b_pointer])
            b_pointer += 1
        else:
            answer.append(nums1[a_pointer])
            a_pointer += 1
    return answer


if __name__ == '__main__':
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))


