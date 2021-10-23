import sys
n = int(sys.stdin.readline())

fib = {
    0: 0,
    1: 1
}

for i in range(n + 1):
    if i not in fib.keys():
        fib[i] = fib[i - 1] + fib[i - 2]

print(fib[n])