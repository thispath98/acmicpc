# https://wook-2124.tistory.com/473 를 참조하였습니다.
N = int(input())
cord = []

for _ in range(N):
    x, y = map(int, input().split())
    cord.append([y, x])

cord = sorted(cord)

for y, x in cord:
    print(x, y)
