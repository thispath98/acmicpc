from itertools import combinations
import sys
N, M = map(int, sys.stdin.readline().split())
combination = list(combinations(range(1, N + 1), M))

for comb in combination:
    print(" ".join(map(str, comb)))
