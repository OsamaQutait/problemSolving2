def merge(nums1, m, nums2, n):
    a_pointer, b_pointer, l_pointer = m - 1, n - 1, m + n - 1
    while b_pointer >= 0:
        if nums1[a_pointer] > nums2[b_pointer] and a_pointer >= 0:
            nums1[l_pointer] = nums1[a_pointer]
            l_pointer -= 1
            a_pointer -= 1
        else:
            nums1[l_pointer] = nums2[b_pointer]
            l_pointer -= 1
            b_pointer -= 1
    return nums1


if __name__ == '__main__':
    print(merge([2,0], 1, [1], 1))


