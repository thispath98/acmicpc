import math
M, N = map(int, input().split())

for i in range(M, N + 1):
    for k in range(2, int(math.sqrt(i)) + 1):
        if i % k == 0:
            break
    else:
        if i > 1: print(i)
