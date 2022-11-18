if __name__ == '__main__':
    my_dict = {
        'Y': 'e',
        'e': 's',
        's': 'Y'
    }
    t = int(input())
    for i in range(t):
        flag = True
        s = str(input())
        if len(s) == 1:
            if my_dict.__contains__(s[0]):
                print('YES')
            else:
                print('NO')
            continue
        for i in range(0, len(s)-1):
            if my_dict.__contains__(s[i+1]) and my_dict.__contains__(s[i]) and s[i + 1] == my_dict.__getitem__(s[i]):
                continue
            else:
                flag = False
                print('NO')
                break
        if flag:
            print('YES')


