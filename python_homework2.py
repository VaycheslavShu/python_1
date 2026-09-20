import os
import sys

from itertools import zip_longest


def MajikSorArr(arr1, arr2)->set:
    arr1_sort = sorted(arr1)
    arr2_sort = sorted(arr2)
    for i, (arr1_sorted, arr2_sorted) in enumerate(
        zip_longest(arr1_sort, arr2_sort, fillvalue="и")
    ):      
        print(f"{i}: {arr1_sorted} {arr2_sorted}")


def main()->set:
    boys = input(
        "Введитите произвольное количество мужских имен: "
    ).replace(",", " ").split()
    girls = input (
        "Введитите произвольное количество женских имен: "
    ).replace(",", " ").split()
    MajikSorArr(boys, girls)



if __name__ == "__main__":
    main()