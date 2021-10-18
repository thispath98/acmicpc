import sys
T = int(sys.stdin.readline())

for _ in range(T):
    result = sys.stdin.readline()
    grade = 0
    count = 0
    seq = False

    for prob in result:
        if prob == 'O':
            count += 1
            seq = True
            grade += count
        else:
            seq = False
            count = 0
    
    print(grade)
