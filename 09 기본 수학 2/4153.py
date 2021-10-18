while True:
    triangle = list(map(int, input().split()))
    max_num = max(triangle)
    triangle.remove(max_num)
    if max_num == 0:
        break
    elif pow(triangle[0], 2) + pow(triangle[1], 2) == pow(max_num, 2):
        print('right')
    else:
        print('wrong')