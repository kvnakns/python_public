
# Bubble Sort:
# A simple algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Track whether a swap has occurred
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if out of order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the list is already sorted
        if not swapped:
            break








# Example Usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(unsorted_list)
print(unsorted_list)  # Output: [11, 12, 22, 25, 34, 64, 90]
