import collections
def firstUniqChar(s: str) -> int:
    answer = -1
    counter = collections.Counter(n for n in s)
    min_num_char = []
    for item, amount in sorted(counter.items(), key=lambda item: item[1]):
        if amount == 1:
            min_num_char.append(item)
    for i in range(len(s)):
        if s[i] in min_num_char:
            answer = i
            break
    return answer

def test_firstUniqChar():
    s = "aabb"
    answer = -1
    assert firstUniqChar(s) == answer