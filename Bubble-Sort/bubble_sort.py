def bubble_sort(sequence):
    unsorted = True
    sorted_index = len(sequence) - 1
    while unsorted:
        unsorted = False
        for i in range(sorted_index):
            if sequence[i] > sequence[i + 1]:
                sequence[i], sequence[i + 1] = sequence[i + 1], sequence[i]
                unsorted = True
        sorted_index = sorted_index - 1
        print(sorted_index)


list_a = [1,3, 2, 11, 4, 9]
bubble_sort(list_a)
print(list_a)
