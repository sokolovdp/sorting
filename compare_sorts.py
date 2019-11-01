import random
from timeit import timeit

from insertion import insertion_sort
from bubble import bubble_sort
from merge import merge_sort
from quick import quick_sort
from tim import tim_sort

N = 1000


if __name__ == '__main__':

    lengths = (19, 101, 500,)
    for length in lengths:
        sequence = [random.randint(0, length) for _ in range(length)]
        t1 = timeit('bubble_sort(sequence)', number=N, globals=globals())
        t2 = timeit('merge_sort(sequence)', number=N, globals=globals())
        t3 = timeit('quick_sort(sequence)', number=N, globals=globals())
        t4 = timeit('insertion_sort(sequence)', number=N, globals=globals())
        t5 = timeit('tim_sort(sequence)', number=N, globals=globals())

        print(
            f'sequence length={len(sequence):4} '
            f'bubble={round(t1, 3):6} '
            f'merge={round(t2, 3):6} '
            f'quick={round(t3, 3):6} '
            f'insertion={round(t4, 3):6} '
            f'tim_sort={round(t5, 3):6} '
        )
