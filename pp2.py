if __name__ == '__main__':
    import numpy as np

    feature_shape = (2, 1000)

    # Create an empty array with shape (0, 2, 2048)
    empty_array = np.empty((0,) + feature_shape)

    print("Empty Array:")
    print(empty_array)
    print("Shape of the Empty Array:", empty_array.shape)

    # t = int(input())
    # for x in range(t):
    #     ms = str(input()).split(' ')
    #     m = int(ms[0])
    #     s = int(ms[1])
    #     y = str(input()).split(' ')
    #     bm = [int(num) for num in y]
    #     bm.sort()
    #     answer = []
    #     i = 1
    #     flag = True
    #     while i <= bm[-1]:
    #         if i != bm[i-1]:
    #             for j in range(i, bm[i-1]):
    #                 if j <= s:
    #                     bm.insert(j-1, j)
    #                     s -= j
    #                 else:
    #                     flag = False
    #                     break
    #         if not flag:
    #             break
    #         i += 1
    #     while s >= bm[-1] + 1:
    #         bm.append(bm[-1] + 1)
    #         s -= bm[-1]
    #     if s == 0 and flag:
    #         print('yes')
    #     else:
    #         print('no')