# 문제를 풀지 못해서 https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%8011000%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EA%B0%95%EC%9D%98%EC%8B%A4-%EB%B0%B0%EC%A0%95를 참조했습니다.
import heapq
import sys

N = int(input())

time_table = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
time_table.sort(key=lambda x: x[0])

queue = []
heapq.heappush(queue,time_table[0][1])

for i in range(1,N):
    if queue[0] > time_table[i][0]: # 강의실이 더 필요한 경우
        heapq.heappush(queue,time_table[i][1])
    else:   # 강의실이 필요 없는 경우
        heapq.heappop(queue)
        heapq.heappush(queue,time_table[i][1])

print(len(queue))