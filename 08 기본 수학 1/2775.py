T = int(input())    # Test Case

for _ in range(T):
    k = int(input())    # 층
    n = int(input())    # 호

    floor_zero = [i for i in range(1, n + 1)]
    if k == 0: print(floor_zero[n - 1])
    else:
        floor_now = floor_zero
        for s in range(1, k + 1):  # 층
            floor_temp = floor_now[:]
            for i in range(1, n):  # 호
                floor_now[i] = sum(floor_temp[0:i + 1])
        print(floor_now[n - 1])