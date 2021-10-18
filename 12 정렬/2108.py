import sys
from collections import Counter

def get_mode(array):
    if len(array) == 1:
        return array[0]

    cnt = Counter(array).most_common(2)
    if cnt[0][1] == cnt[1][1]:
        return cnt[1][0]

    return cnt[0][0]

N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline()) for _ in range(N)]
numbers.sort()

print(round(sum(numbers) / N))
print(numbers[N//2])
print(get_mode(numbers))
print(numbers[-1] - numbers[0])
