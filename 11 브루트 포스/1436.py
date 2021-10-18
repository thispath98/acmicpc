# 정답은 맞았지만 while 문으로 구현하는 방법은
# [https://pacific-ocean.tistory.com/137]를 참조하였습니다.
N = int(input())

sequel = 666
count = 0
while True:
    if '666' in str(sequel):
        count += 1

        if count == N:
            print(sequel)
            break
    sequel += 1