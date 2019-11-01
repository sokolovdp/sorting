
def partition(arr, low, high):
    """
    This function takes last element as pivot, places
    the pivot element at its correct position in sorted
    array, and places all smaller (smaller than pivot)
    to left of pivot and all greater elements to right
    of pivot
    :param arr: array to sort
    :param low: starting index
    :param high: ending index
    :return:
    """
    pos = low  # index of smaller element
    pivot = arr[high]  # pivot
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] < pivot:
            # increment index of smaller element
            arr[pos], arr[j] = arr[j], arr[pos]
            pos += 1

    arr[pos], arr[high] = arr[high], arr[pos]
    return pos


def quick_sort_recursive(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[p] is now at right place
        pi = partition(arr, low, high)

        # Separately sort elements before partition and after partition
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)
    return arr


def quick_sort(arr):
    if not arr or len(arr) < 2:
        return arr
    return quick_sort_recursive(arr, 0, len(arr) - 1)
