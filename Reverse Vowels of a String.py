def reverseVowels(s: str) -> str:
    s = list(s)
    vowels = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True, 'A': True, 'E': True, 'I': True, 'O': True, 'U': True}
    left_pointer, right_pointer = 0, len(s) - 1
    while left_pointer <= right_pointer:
        try:
            if vowels.__contains__(s[left_pointer]) and vowels.__contains__(s[right_pointer]):
                s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
                left_pointer += 1
                right_pointer -= 1
            if not vowels.__contains__(s[left_pointer]):
                left_pointer += 1
            if not vowels.__contains__(s[right_pointer]):
                right_pointer -= 1
        except IndexError:
            break
    return ''.join(s)

if __name__ == '__main__':
    print(reverseVowels("aA"))
