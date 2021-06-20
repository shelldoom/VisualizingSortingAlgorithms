from p5 import *
from random import sample

def merge(arr1: list[int], arr2: list[int]):
    result = []
    n1 = len(arr1)
    n2 = len(arr2)
    i, j = 0, 0
    while i < n1 or j < n2:
        if i >= n1:
            result.append(arr2[j])
            j += 1
        elif j >= n2:
            result.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    return result

def merge_sort(arr: list[int]):
    if len(arr) == 1:
        return arr
    if len(arr) == 2:
        return (arr[0] <= arr[1])*[arr[0], arr[1]] + (arr[0] > arr[1]) * [arr[1], arr[0]]

    n = len(arr) // 2
    arr1 = merge_sort(arr[:n])
    arr2 = merge_sort(arr[n:])
    return merge(arr1, arr2)