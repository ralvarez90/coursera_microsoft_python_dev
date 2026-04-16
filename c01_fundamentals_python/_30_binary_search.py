"""
ALGORITMO BÚSQUEDA BINARIA
"""
from random import randint


def binarySearch(data: list, target):
    """
    Performs a binary search to find the target element within a sorted list

    Args:
        data (list): The sorted list of elements to search through,
        target: The element to search for.

    Raises:
        ValueError: In case thatn data cannot be a list
    Returns:
        int: The index of the target if found. -1 otherwhise.
    """

    # Verify of data is a list
    if not isinstance(data, list):
        raise ValueError('The data is not a list.')

    # Verify an empty list case
    if not data:
        return -1

    # Initialize the beginning and ending indexes.
    low = 0
    high = len(data) - 1

    # Continue searching as long as the lower bound is less than or equal to the upper bouind
    while low <= high:

        # Calculate the middle index, use integer division
        mid = (low + high) // 2

        # Check if the element at the middle index is the target
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    # Case if target dont found
    return -1


# Run application.
if __name__ == '__main__':
    # Create a list with random numbers and sort.
    listExample = list(set([randint(1, 1_000_000) for _ in range(1_000_000)]))
    listExample.sort()

    # Use binary search to find the target element
    print(f'Searching {listExample[-1]} in list_example...')
    print(binarySearch(data=listExample, target=listExample[-1]))
