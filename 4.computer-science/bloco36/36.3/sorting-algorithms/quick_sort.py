def quick_sort(numbers, start, end):
    if start < end:
        p = partition(numbers, start, end)
        quick_sort(numbers, start, p - 1)
        quick_sort(numbers, p + 1, end)

# função auxiliar responsável pela partição do array
# escolhendo um pivô e fazendo movimentações dos sub arrays gerados


def partition(numbers, start, end):
    pivot = numbers[end]
    delimiter = start - 1

    for index in range(start, end):
        if numbers[index] <= pivot:
            delimiter = delimiter + 1
            x, y = index, delimiter
            numbers[x], numbers[y] = numbers[y], numbers[x]

    numbers[delimiter + 1], numbers[end] = numbers[end], numbers[delimiter + 1]

    return delimiter + 1
