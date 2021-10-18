word = input()
modified = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
count = 0

for mo in modified:
    count += word.count(mo)
    
print(len(word) - count)