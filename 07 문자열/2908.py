A, B = map(str, input().split())
A = A[::-1]
B = B[::-1]
print(A if A > B else B)