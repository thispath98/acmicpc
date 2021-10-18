import sys
T = int(input())
for i in range(T):
    R, in_str = sys.stdin.readline().split()
    for str in in_str:
        print(str * int(R), end="")
    print()
