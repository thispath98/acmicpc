R, C = map(int, input().split())
island_map = [list(input()) for row in range(R)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def print_map_after_fifty_years_after(R, C, map):
    island_list = [[row, col] for row in range(R) for col in range(C) if map[row][col] == 'X' ]
    vanishing_list = []

    for island in island_list:
        count = 0
        for i in range(4):
            row = island[0] + dr[i]
            col = island[1] + dc[i]
            if row < 0 or row >= R or col >= C or col < 0 or map[island[0] + dr[i]][island[1] + dc[i]] == '.':
                count += 1
        if count >= 3:
            vanishing_list.append([island[0], island[1]])

    for vanished in vanishing_list:
        map[vanished[0]][vanished[1]] = '.'

    island_row = [row for row in range(R) for col in range(C) if map[row][col] == 'X' ]
    island_col = [col for row in range(R) for col in range(C) if map[row][col] == 'X' ]

    if island_row:
        for i in range(min(island_row), max(island_row) + 1):
            for j in range(min(island_col), max(island_col) + 1):
                print(map[i][j], end='')
            print()
    else:
        print('X')


print_map_after_fifty_years_after(R, C, island_map)