def heapify(arr, heap_size, root_index):
    """
    Ensures the subtree rooted at root_index satisfies the max-heap property.
    """
    largest = root_index  # Initialize largest as root
    left_child = 2 * root_index + 1  # Left child index
    right_child = 2 * root_index + 2  # Right child index

    # Check if the left child is larger than the root
    if left_child < heap_size and arr[left_child] > arr[largest]:
        largest = left_child

    # Check if the right child is larger than the largest so far
    if right_child < heap_size and arr[right_child] > arr[largest]:
        largest = right_child

    # If the largest is not the root, swap and continue heapifying
    if largest != root_index:
        arr[root_index], arr[largest] = arr[largest], arr[root_index]  # Swap
        heapify(arr, heap_size, largest)  # Recursively heapify the affected subtree


def heap_sort(arr):
    """
    Sorts an array in ascending order using the Heap-Sort algorithm.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move current root to the end
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        # Call heapify on the reduced heap
        heapify(arr, i, 0)


# Test the algorithm
if __name__ == "__main__":
    array = [12, 11, 13, 5, 6, 7]
    print("Original array:")
    print(array)

    heap_sort(array)

    print("\nSorted array:")
    print(array)
