def countVowelSubstrings(word: str) -> int:
    vowels = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    count, j = 0, 0
    for char in word:
        if vowels.__contains__(char):
            vowels.__setitem__(char, vowels.__getitem__(char)+1)
        else:
            vowels.__setitem__(char, 1)
        flag = True
        for value in vowels.values():
            if value == 0:
                flag = False
        # if flag:
            # while


if __name__ == '__main__':
    print(countVowelSubstrings("cuaieuouac"))
