import sys
from itertools import permutations
N, M = map(int, sys.stdin.readline().split())
permutation = list(permutations(list(range(1, N+1)), M))

for permute in permutation:
    print(" ".join(map(str,permute)))
