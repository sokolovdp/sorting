from timeit import timeit
import random

N = 1000


def bubble_sort(arr):
    if not arr or len(arr) < 2:
        return arr

    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def split_list(arr):
    n = len(arr)
    m = n // 2
    return arr[:m], arr[m:]


def merge_sorted_lists(list_left, list_right):
    """
    Merge two sorted lists
    This is a linear operation
    O(len(list_right) + len(list_right))
    :param list_left: list
    :param list_right: list
    :return merged list
    """
    len_list_left = len(list_left)
    len_list_right = len(list_right)

    # Special case: one or both of lists are empty
    if len_list_left == 0:
        return list_right
    elif len_list_right == 0:
        return list_left

    index_left = index_right = 0
    list_merged = []  # list to build and return
    list_len_target = len_list_left + len_list_right
    while len(list_merged) < list_len_target:
        if list_left[index_left] <= list_right[index_right]:
            # Value on the left list is smaller (or equal so it should be selected)
            list_merged.append(list_left[index_left])
            index_left += 1
        else:
            # Right value bigger
            list_merged.append(list_right[index_right])
            index_right += 1

        # If we are at the end of one of the lists we can take a shortcut
        if index_right == len_list_right:
            # Reached the end of right
            # Append the remainder of left and break
            list_merged.extend(list_left[index_left:])
            break
        elif index_left == len_list_left:
            # Reached the end of left
            # Append the remainder of right and break
            list_merged.extend(list_right[index_right:])
            break

    return list_merged


def merge_sort(arr):
    if not arr or len(arr) < 2:
        return arr
    left, right = split_list(arr)
    # This line is the most important piece in this whole thing
    return merge_sorted_lists(merge_sort(left), merge_sort(right))


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


def insertion_sort(arr):
    if len(arr) < 2:
        return arr

    for i in range(1, len(arr)):
        current_value = arr[i]
        position = i
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position = position - 1
        arr[position] = current_value

    return arr


if __name__ == '__main__':
    test = [16, 1, 9, 10, 10, 11]
    insertion_sort(test)
    print(test)

    lengths = (19, 101, 500,)
    for length in lengths:
        sequence = [random.randint(0, length) for _ in range(length)]
        t1 = timeit('bubble_sort(sequence)', number=N, globals=globals())
        t2 = timeit('merge_sort(sequence)', number=N, globals=globals())
        t3 = timeit('quick_sort(sequence)', number=N, globals=globals())
        t4 = timeit('insertion_sort(sequence)', number=N, globals=globals())

        print(
            f'sequence length={len(sequence)} '
            f'bubble={round(t1, 3)} '
            f'merge={round(t2, 3)} '
            f'quick={round(t3, 3)} '
            f'insertion={round(t4, 3)}'
        )
