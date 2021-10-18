N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_card = 0
for i in cards[:-2]:
    for j in cards[cards.index(i) + 1:-1]:
        for k in cards[cards.index(j) + 1:]:
            if max_card < i + j + k < M + 1:
                max_card = i + j + k

print(max_card)
