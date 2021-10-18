# https://god-gil.tistory.com/62 의 도움을 받았습니다.
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def get_min_count_of_printing(chess):
    black_chess = [['B' if (i + j) % 2 == 0 else 'W' for i in range(8)] for j in range(8)]
    result = []
    for row in range(N - 7):
        for col in range(M - 7):
            black_count = 0
            white_count = 0
            
            for i in range(8):
                for j in range(8):
                    if chess[row + i][col + j] == black_chess[i][j]:
                        black_count += 1
                    else:
                        white_count += 1

            result.append(min(black_count, white_count))

    return min(result)


print(get_min_count_of_printing(board))