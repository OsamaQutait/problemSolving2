def solution(numbers, left, right):
    answer = []
    for i in range(len(numbers)):
        print(numbers[i] / (i + 1))
        x = numbers[i] / (i + 1)
        if x % 1 == 0:
            x = int(x)
        else:
            x = x
        if isinstance(x, int):
            if left <= (x) <= right:
                answer.append(True)
            else:
                answer.append(False)
        else:
            answer.append(False)
    return answer

def solution1(a):
    b = []
    a_pointer = 0
    b_pointer = len(a) - 1
    flag = True
    while a_pointer < b_pointer:
        b.append(a[a_pointer])
        b.append(a[b_pointer])
        a_pointer += 1
        b_pointer -= 1
        if a_pointer == b_pointer:
            b.append(a[b_pointer])
    i = 1
    while i < len(b):
        if b[i] > b[i - 1]:
            i += 1
        else:
            flag = False
            break
    return flag
def solution2(s1, s2):
    answer = ""
    if len(s1) > len(s2):
        return s2 + s1
    elif len(s1) < len(s2):
        return s1 + s2
    else:
        i = 0
        j = 0
        while True:
            try:
                if s1[i] > s2[j]:
                    answer += s2[j]
                    j += 1
                else:
                    answer += s1[i]
                    i += 1
            except IndexError:
                break
        return answer

if __name__ == '__main__':
    print(solution2("super", "tower"))