import collections
def frequencySort(s: str) -> str:
    answer = ""
    counter = collections.Counter(n for n in s)
    for item, amount in sorted(counter.items(), key=lambda item: item[1], reverse=True):
        answer += item*amount
    return answer
def test_frequencySort():
    s = "raaeaedere"
    answer = "eeeeaaarrd"
    assert frequencySort(s) == answer
