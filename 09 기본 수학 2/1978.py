N = int(input())
is_prime = list(map(int, input().split()))

count = 0
for num in is_prime:
    if num == 1: count += 1; continue
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            count += 1
            break

print(N - count)