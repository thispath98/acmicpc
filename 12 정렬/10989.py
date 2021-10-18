import sys
N = int(sys.stdin.readline())
numbers = {}
for _ in range(N):
    number = int(sys.stdin.readline().strip())
    if number in numbers:
        numbers[number] += 1
    else:
        numbers[number] = 1

for number in sorted(numbers):
    for _ in range(numbers[number]):
        print(number)
        