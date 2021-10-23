from itertools import combinations_with_replacement
import sys
N, M = map(int, sys.stdin.readline().split())
combination = list(combinations_with_replacement(range(1, N + 1), M))

for comb in combination:
    print(" ".join(map(str, comb)))
