import sys
C = int(input())

for i in range(C):
    numbers = list(map(float, sys.stdin.readline().split()))
    avg_num = sum(numbers[1:]) / len(numbers[1:])
    count = 0
    for number in numbers[1:]:
        if number > avg_num:
            count += 1
    ratio = count / len(numbers[1:]) * 100
    print(f'{ratio:.3f}%')