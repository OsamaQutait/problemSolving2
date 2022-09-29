def addBinary(a: str, b: str) -> str:
    answer, carry = "", "0"
    a_len, b_len = len(a), len(b)
    max_len = max(a_len, b_len)
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    for i in reversed(range(max_len)):
        if a[i] == "1" and b[i] == "1":
            if carry == "1":
                answer = "1" + answer
                carry = "1"
            else:
                answer = "0" + answer
                carry = "1"
        elif (a[i] == "0" and b[i] == "1") or (a[i] == "1" and b[i] == "0"):
            if carry == "0":
                answer = "1" + answer
            else:
                answer = "0" + answer
        else:
            answer = carry + answer
            carry = "0"
    if carry == "1":
        answer = carry + answer
    return answer


def test():
    a = "11"
    b = "1"
    answer = "10101"
    assert addBinary(a, b) == answer

# if __name__ == '__main__':
#     print(addBinary("11", "1"))

