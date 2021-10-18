word = input()
second = 0
for alphabet in word:
    dial = ord(alphabet) - ord('A')
    if dial < 15:
        dial_num = dial // 3 + 2
    elif dial < 19:
        dial_num = 7
    elif dial < 22:
        dial_num = 8
    else:
        dial_num = 9
    second += dial_num + 1
print(second)