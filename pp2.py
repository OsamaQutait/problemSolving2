if __name__ == '__main__':
    t = int(input())
    for x in range(t):
        ms = str(input()).split(' ')
        m = int(ms[0])
        s = int(ms[1])
        y = str(input()).split(' ')
        bm = [int(num) for num in y]
        bm.sort()
        answer = []
        i = 1
        flag = True
        while i <= bm[-1]:
            if i != bm[i-1]:
                for j in range(i, bm[i-1]):
                    if j <= s:
                        bm.insert(j-1, j)
                        s -= j
                    else:
                        flag = False
                        break
            if not flag:
                break
            i += 1
        while s >= bm[-1] + 1:
            bm.append(bm[-1] + 1)
            s -= bm[-1]
        if s == 0 and flag:
            print('yes')
        else:
            print('no')