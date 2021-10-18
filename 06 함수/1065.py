def count_han(num):
    num_of_han = 0
    if num <= 99:
        num_of_han = num
    else:
        for is_han in range(100, num + 1):
            str_num = str(is_han)
            for i in range(len(str_num) - 2):
                if int(str_num[i + 2]) - int(str_num[i + 1]) != int(str_num[i + 1]) - int(str_num[i]):
                    break
                num_of_han += 1
        num_of_han += 99
    return num_of_han


if __name__ == "__main__":
    N = int(input())
    print(count_han(N))