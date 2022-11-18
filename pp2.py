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
        for i in range(1, m):
            if bm[i-1] != i:
                for j in range(i, bm[i-1]):
                    if s >= j:
                        answer.append(j)
                        s -= j
                    else:
                        break
            else:
                answer.append(i)
        while s > answer[-1]:
            answer.append(answer[-1]+1)
            s -= answer[-1]+1

        print(answer)