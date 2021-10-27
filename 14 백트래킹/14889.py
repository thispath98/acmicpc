from itertools import combinations, permutations
import sys
N = int(sys.stdin.readline())
stat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

number_of_team_member = N // 2
stat_combination = number_of_team_member * (number_of_team_member - 1)

stat_gap = stat_combination * 99

team_combination = list(combinations(list(range(N)), number_of_team_member))

for i in range(len(team_combination) // 2):
    start_team = team_combination[i]
    link_team = team_combination[-(i + 1)]
    
    start_team_permutation = list(permutations(list(start_team), 2))
    link_team_permutation = list(permutations(list(link_team), 2))
    
    stat_of_start_team = 0
    for i, j in start_team_permutation:
        stat_of_start_team += stat[i][j]

    stat_of_link_team = 0
    for i, j in link_team_permutation:
        stat_of_link_team += stat[i][j]
    
    if stat_gap > abs(stat_of_start_team - stat_of_link_team):
        stat_gap = abs(stat_of_start_team - stat_of_link_team)

print(stat_gap)