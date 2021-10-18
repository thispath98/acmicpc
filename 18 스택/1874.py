N = int(input())

seq = [int(input()) for _ in range(N)]
seq_idx = 0

stack = []
i = 1
oper = []

while seq_idx < len(seq):
    if  not stack or stack[-1] < seq[seq_idx]:
        stack.append(i)
        i += 1
        oper.append('+')
    elif stack[-1] == seq[seq_idx]:
        stack.pop()
        oper.append('-')
        seq_idx += 1
    else:
        oper.clear()
        oper.append('NO')
        break

for operation in oper:
    print(operation)