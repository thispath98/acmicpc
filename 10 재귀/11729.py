# 혼자 힘으로 풀지 못해 [https://claude-u.tistory.com/127]를 참조했습니다.
def hanoi(plates, start, mid, dest):
    if plates == 1:
        print(start, dest)
    else:
        hanoi(plates - 1, start, dest, mid)
        print(start, dest)
        hanoi(plates - 1, mid, start, dest)

N = int(input())
print(2 ** N - 1)
hanoi(N, 1, 2, 3)