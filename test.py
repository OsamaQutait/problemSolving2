if __name__ == '__main__':
    a = [1,2,8,55,65,15,774,55]
    print(len(a))
    for i in range(18):
        try:
            print(a[i])
        except IndexError:
            print("error")
            break