import sys
A, B, C = map(int, sys.stdin.readline().split())

income = C - B
if income <= 0:
    print(-1)
elif A < income:
    print(1)
elif A % income >= 0:
    print(A // income + 1)