def insertion_sort(numbers):
    n = len(numbers)

    for index in range(1, n):
        key = numbers[index]

        new_position = index - 1
        while new_position >= 0 and numbers[new_position] > key:
            numbers[new_position + 1] = numbers[new_position]
            new_position = new_position - 1

        numbers[new_position + 1] = key

    return numbers
