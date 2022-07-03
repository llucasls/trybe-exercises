def bubble_sort(numbers):
    n = len(numbers)

    for ordered_elements in range(n - 1):
        for item in range(0, n - 1 - ordered_elements):
            item2 = item + 1
            if numbers[item] > numbers[item2]:
                numbers[item], numbers[item2] = numbers[item2], numbers[item]

    return numbers
