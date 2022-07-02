def selection_sort(numbers):
    n = len(numbers)

    for index in range(n - 1):
        min_element_index = index

        for search_index in range(index + 1, n):
            if numbers[search_index] < numbers[min_element_index]:
                min_element_index = search_index

        # Troca os elementos de posição
        index2 = min_element_index
        numbers[index], numbers[index2] = numbers[index2], numbers[index]

    return numbers
