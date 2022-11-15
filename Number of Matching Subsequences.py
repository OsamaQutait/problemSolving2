from typing import *
from collections import Counter
def numMatchingSubseq(s: str, words: List[str]) -> int:
    counter = 0
    words_dict = Counter(words)
    for word, value in words_dict.items():
        i = 0
        for char in s:
            if i < len(word):
                if char == word[i]:
                    i += 1
            else:
                break
        if i == len(word):
            counter += words_dict.__getitem__(word)
    return counter

if __name__ == '__main__':
    print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))