M = int(input())
N = int(input())

prime = []
for i in range(M, N + 1):
    if i == 1: continue
    for j in range(2, i // 2 + 1):
        if i % j == 0: break
    else: 
        prime.append(i)

if prime:
    print(sum(prime))
    print(prime[0])
else:
    print(-1)