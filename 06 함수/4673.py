def print_self_number(n):
    nums = list(range(1, n + 1))
    for num in nums[:]:
        digits = []
        digit = num

        for _ in range(len(str(digit))):
            digits.append(digit % 10)
            digit = digit // 10
        
        self_number = num + sum(digits)
        if self_number in nums:
            nums.remove(self_number)
            
    for num in nums:
        print(num)

if __name__ == "__main__":
    print_self_number(10000)
