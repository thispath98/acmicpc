# https://zidarn87.tistory.com/339 와 https://claude-u.tistory.com/245 를 참고했다. 하지만 이해되지 않는다.
import sys
N = int(sys.stdin.readline())
cases = 0
board = [0] * 15

def check(depth):
    for i in range(depth):
        if board[depth] == board[i] or abs(board[i] - board[depth]) == depth - i:
            return False
    return True

def dfs(depth):
    global cases
    if depth == N:
        cases += 1
        return
    for i in range(N):
        board[depth] = i
        if check(depth):
            dfs(depth + 1)

dfs(0)
print(cases)