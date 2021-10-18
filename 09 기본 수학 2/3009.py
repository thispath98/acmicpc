import collections
A, B = map(int, input().split())
C, D = map(int, input().split())
E, F = map(int, input().split())

count = collections.Counter([A, C, E])
G = count.most_common(2)[1][0]
count = collections.Counter([B, D, F])
H = count.most_common(2)[1][0]
print(G, H)