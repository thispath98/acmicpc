import sys

T = int(sys.stdin.readline())
N = [int(sys.stdin.readline()) for _ in range(T)]

fibo = {0: (1, 0), 1: (0, 1)}


def get_fibo_count(n):
    if n not in fibo.keys():
        fibo[n] = (
            get_fibo_count(n - 1)[0] + get_fibo_count(n - 2)[0],
            get_fibo_count(n - 1)[1] + get_fibo_count(n - 2)[1],
        )
    return fibo[n]


get_fibo_count(max(N))

for n in N:
    print(fibo[n][0], fibo[n][1])
