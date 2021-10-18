N = int(input())
layer = 1
count = 1
find = False
while find != True:
    count += 6 * (layer - 1)
    if(N <= count):
        find = True
    else:
        layer += 1
print(layer)