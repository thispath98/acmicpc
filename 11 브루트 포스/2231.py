def get_sum_of_digits(num):
    digit = [num % 10]
    while num >= 10:
        num = num // 10
        digit.append(num % 10)

    return sum(digit)

N = int(input())

constructor = N // 2
for num in range(constructor, N + 1):
    if num + get_sum_of_digits(num) == N:
        print(num)
        break
else:
    print(0)