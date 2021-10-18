T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split()) # H: 층 수, W: 방 수, N: 손님의 순서
    ho = N // H + 1 if N % H != 0 else N // H
    floor = N % H if N % H != 0 else H
    print(f'{floor}{ho:02d}')