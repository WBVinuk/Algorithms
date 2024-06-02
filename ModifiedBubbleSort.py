def modified_bubble_sort(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                # Swap the elements
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        # You can also reduce the range of the loop as the last elements are already sorted
        n -= 1

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
modified_bubble_sort(arr)
print("Sorted array:", arr)
