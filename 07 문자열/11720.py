import sys
N = sys.stdin.readline()
numbers = list(map(int, input()))
sum = 0
for number in numbers:
    sum += int(number)
print(sum)