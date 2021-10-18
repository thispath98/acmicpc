N = int(input())
factorial = 1
for i in range(N):
    factorial *= (N - i)
print(factorial)