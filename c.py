def inter(num1, num2):
    dict_num1 = {}
    dict_num2 = {}
    x = []
    for num in num1:
        if dict_num1[num]:
            dict_num1[num] += 1
        else:
            dict_num1[num] = 1

    for num in num2:
        if dict_num2[num]:
            dict_num2[num] += 1
        else:
            dict_num2[num] = 1

    for i in dict_num1.values():
        for j in dict_num2.values():
            if i == j:
                x.push([i] * min(dict_num1[i], dict_num2[j]))
    return x




if __name__ == '__main__':
    # print(inter([1,2,2,1], [2,2]))
    for i in range(65, 91):
        print(chr(i), "->", i-65)