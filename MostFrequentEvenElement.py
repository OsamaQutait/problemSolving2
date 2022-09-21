import collections
def mostFrequentEven(nums):
    answer = -1
    max_amount = 0
    num = collections.Counter(n for n in nums if n % 2 == 0)
    for item, amount in num.items():
        if amount > max_amount or(amount == max_amount and answer > item):
            answer = item
            max_amount = amount
    return answer
if __name__ == '__main__':
    print(mostFrequentEven([8154,9139,8194,3346,5450,9190,133,8239,4606,8671,8412,6290]))
    