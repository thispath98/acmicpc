import math

while True:
    n = int(input())
    if n == 0: break

    prime_count = 0
    for i in range(n + 1, 2 * n + 1):
        for k in range(2, int(math.sqrt(i)) + 1):
            if i % k == 0:
                break
        else:
            prime_count += 1
    print(prime_count)