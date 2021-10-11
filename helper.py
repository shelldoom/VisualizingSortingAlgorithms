
def bubbleSort(arr: list[int]):
    n = len(arr) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n):
            yield list(arr), {(i, "yellow"), (i + 1, "darkgoldenrod")}
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield list(arr), {(i, "red"), (i+1, "red")}
        n-=1

def insertionSort(arr: list[int]):
    sorted_size = 0
    n = len(arr)
    while sorted_size < n:
        j = sorted_size
        while j - 1 >= 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            yield list(arr), {(j, "red"), (j-1, "red")}
        sorted_size += 1

# Merge sort is incomplete
def mergeSort(arr, lo=None, hi=None):
    if lo == None and hi == None:
        lo, hi = 0, len(arr) 
    if lo < hi:
        mid = int((lo+hi)/2)
        yield from mergeSort(arr, lo, mid)
        yield from mergeSort(arr, mid+1, hi)
        yield from merge(arr, lo, mid, hi)

def merge(arr, left, mid, right):
    L, R = arr[left:mid+1], arr[mid+1:right+1]
    i, j = 0, 0
    k = left
    while i < len(L) and j < len(R):
        yield arr, [left+i, mid+j], [left, mid, right]
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def quickSort(arr: list[int]):
    # Pivot - Blue Color
    # i - yellow
    # j - dark golden
    def _qs(arr, start=0, end=len(arr)-1):
        if start > end: return
        pivot = arr[start]
        i, j = start, end
        yield list(arr), [(i, "yellow"), (j, "darkgoldenrod1")]
        while i < j:
            while i < len(arr) and arr[i] <= pivot:
                i+=1
                yield list(arr), [(start, "blue"), (i, "yellow"), (j, "darkgoldenrod1")]
            while arr[j] > pivot :
                j-=1
                yield list(arr), [(start, "blue"), (i, "yellow"), (j, "darkgoldenrod1")]
            if i < j:
                yield list(arr), [(i, "red"), (j, "red"), (start, "blue")]
                arr[i], arr[j] = arr[j], arr[i]
                yield list(arr), [(i, "red"), (j, "red"), (start, "blue")]
            else:
                yield list(arr), [(start, "blue"), (i, "yellow"), (j, "darkgoldenrod1")]
        yield list(arr), [(start, "red"), (j, "red")]
        arr[j], arr[start] = arr[start], arr[j]
        yield list(arr), [(j, "blue"), (start, "red")]
        yield from _qs(arr, start, j-1)
        yield from _qs(arr, j+1, end)
    return _qs(arr)


def heapSort(arr: list[int]):
    pass

