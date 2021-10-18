# 시간 초과를 해결하지 못해 https://gudwns1243.tistory.com/52를 참고했음
import sys
N = int(sys.stdin.readline())
cords = list(map(int, sys.stdin.readline().split()))
sorted_cords = sorted(set(cords))

compressed_cords = {sorted_cords[i]: i for i in range(len(sorted_cords))}

for cord in cords:
    print(compressed_cords[cord], end=" ")
