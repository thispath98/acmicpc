X = int(input())

layer = 1
iter = 0
numerator = 1
denominator = 1

while True:
    if layer * (layer + 1) // 2 >= X:
        iter = X - layer * (layer - 1) // 2 - 1
        break
    layer += 1

if layer % 2 == 0: denominator = layer - iter; numerator = 1 + iter 
else: numerator = layer - iter; denominator = 1 + iter
print(f'{numerator}/{denominator}')