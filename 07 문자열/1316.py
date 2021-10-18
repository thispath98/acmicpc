N = int(input())
count = 0
for _ in range(N):
    words = input()
    idx = 0
    is_group_num = True
    while idx < len(words):
        alphabet = words[idx]
        words_count = words.count(alphabet)
        idx += words_count
        if alphabet in words[idx:]:
            is_group_num = False
            break
    if is_group_num == True: count += 1 

print(count)