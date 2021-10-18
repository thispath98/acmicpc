import math

def is_not_prime(num):
    for k in range(2, int(math.sqrt(num)) + 1):
        if num % k == 0:
            return True
    else:
        return False

T = int(input())
for _ in range(T):
    num = int(input())
    partition = [num //2, num // 2]

    while is_not_prime(partition[0]) or is_not_prime(partition[1]):
        partition[0] -= 1
        partition[1] += 1

    print(partition[0], partition[1])
