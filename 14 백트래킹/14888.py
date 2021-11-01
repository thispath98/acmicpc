# 문제 풀이 방법은 스스로 생각했지만 
# https://velog.io/@kimdukbae/BOJ-14888-연산자-끼워넣기-Python 를 참고하였다.
from itertools import permutations
import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
operation_count = list(map(int, sys.stdin.readline().split()))

operation_sequence = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: int(x / y)
}

operations = []
for i in range(4):
    operations.extend(operation_count[i] * list(operation_sequence.keys())[i])

maximum = -(sys.maxsize + 1)
minimum = sys.maxsize

for case in permutations(operations, N - 1):
    total = A[0]
    for j in range(1, N):
        total = operation_sequence[case[j - 1]](total, A[j])

    if total > maximum:
        maximum = total
    if total < minimum:
        minimum = total


print(maximum)
print(minimum)
