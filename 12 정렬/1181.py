N = int(input())
words = [input() for _ in range(N)]

def sort_by_length(array):
    lengths = {}
    for element in array:
        if len(element) in lengths:
            lengths[len(element)].add(element)
            pass
        else:
            lengths[len(element)] = set([element])

    sorted_lengths = sorted(lengths.items())
    for key, value in sorted_lengths:
        listed_value = list(value)
        for sorted_value in sorted(listed_value):
            print(sorted_value)

sort_by_length(words)