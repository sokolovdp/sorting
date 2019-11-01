
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

