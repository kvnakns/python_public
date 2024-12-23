
# Binary Search:
# Binary Search is an efficient algorithm for finding an element in a SORTED list. 
# It works by repeatedly dividing the search interval in half.


def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        # Calculate the middle index
        mid = left + (right - left) // 2  # Prevents potential overflow

        # Check if the target is at the mid index
        if arr[mid] == target:
            return mid  # Return the index of the target

        # If the target is smaller, discard the right half
        elif arr[mid] > target:
            right = mid - 1

        # If the target is larger, discard the left half
        else:
            left = mid + 1

    return -1  # Return -1 if the target is not found








# Example Usage
sorted_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]
target = 7

result = binary_search(sorted_list, target)
if result != -1:
    print(f"Element found at index {result}")  # Output: Element found at index 3
else:
    print("Element not found")
