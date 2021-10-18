words = input()
words = words.upper()
list = [-1 for i in range(ord('Z') - ord('A') + 1)]

for index, word in enumerate(words):
    list_index = ord(word) - ord('A')
    list[list_index] += 1
    
max_num = max(list)
if max_num in list[list.index(max_num) + 1:]:
    print('?')
else:
    print(chr(ord('A') + list.index(max_num)))