# 정답은 맞았지만 한 줄에 출력하는 방법을 참고하였습니다.
N = list(input())
sorted_N = sorted(N, reverse=True)
print(''.join(sorted_N))