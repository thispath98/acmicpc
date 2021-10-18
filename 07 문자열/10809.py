S = input()
position = [-1 for i in range(ord('z') - ord('a') + 1)]
count = 0
for alphabet in S:
    position_in_list = ord(alphabet) - ord('a')
    if position[position_in_list] == -1:
        position[position_in_list] = count
    count += 1

for i in position:
    print(i, end=" ")