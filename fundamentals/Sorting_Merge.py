
# Merge Sort
# A recursive algorithm that divides the array into halves, sorts them, and merges the sorted halves

def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: A single element is already sorted

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)



def merge(left, right):
    sorted_array = []
    i = j = 0

    # Compare and merge the elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # Add remaining elements from both halves
    sorted_array.extend(left[i:])
    sorted_array.extend(right[j:])
    return sorted_array





# Example Usage
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print(sorted_list)  # Output: [3, 9, 10, 27, 38, 43, 82]
