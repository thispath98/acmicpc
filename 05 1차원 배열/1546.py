import sys
N = int(sys.stdin.readline())
test = list(map(float, sys.stdin.readline().split()))

mp = 100 / max(test)

for key, value in enumerate(test):
    test[key] = value * mp

print(sum(test) / len(test))