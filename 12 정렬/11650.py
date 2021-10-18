import sys
N = int(sys.stdin.readline())
cords = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

cords.sort(key = lambda x: x[1])
cords.sort(key = lambda x: x[0])
for i in range(N):
    print(cords[i][0], cords[i][1])