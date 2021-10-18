import sys
N = int(sys.stdin.readline())
numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
for number in sorted(numbers):
    print(number)