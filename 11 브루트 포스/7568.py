def print_big_guy(N):
    big_guy_list = [list(map(int,input().split())) for _ in range(N)]

    rank = [1] * N
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            if big_guy_list[i][0] < big_guy_list[j][0] and big_guy_list[i][1] < big_guy_list[j][1]:
                rank[i] += 1

    for ranks in rank:
        print(ranks, end=' ')

N = int(input())
print_big_guy(N)