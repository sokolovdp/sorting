# based off of this code https://gist.github.com/nandajavarma/a3a6b62f34e74ec4c31674934327bbd3

from insertion import insertion_sort


def merge(left, right):
    """
    Takes two sorted lists and returns a single sorted list by comparing the elements one at a time.
    """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def tim_sort(the_array):
    runs, sorted_runs = [], []
    length = len(the_array)
    new_run = [the_array[0]]

    for i in range(1, length):
        if i == length - 1:  # if i is at the end of the list
            new_run.append(the_array[i])
            runs.append(new_run)
            break
        # if the i'th element of the array is less than the one before it
        if the_array[i] < the_array[i - 1]:
            if not new_run:
                runs.append([the_array[i]])
            else:
                runs.append(new_run)
                new_run = []
        new_run.append(the_array[i])

    # for every item in runs, append it using insertion sort
    for item in runs:
        sorted_runs.append(insertion_sort(item))

    # for every run in sorted_runs, merge them
    sorted_array = []
    for run in sorted_runs:
        sorted_array = merge(sorted_array, run)

    return sorted_array

