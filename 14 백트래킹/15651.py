import sys
from itertools import product
N, M = map(int, sys.stdin.readline().split())
products = list(product(list(range(1, N+1)), repeat=M))

for prod in products:
    print(" ".join(map(str,prod)))
