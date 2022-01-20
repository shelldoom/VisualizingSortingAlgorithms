
def bubbleSort(arr: list[int]):
    n = len(arr) - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(0, n):
            yield list(arr), {(i, "darkorange"), (i + 1, "gold")}
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
                yield list(arr), {(i, "indianred"), (i+1, "indianred")}
        n-=1

def insertionSort(arr: list[int]):
    sorted_size = 0
    n = len(arr)
    while sorted_size < n:
        j = sorted_size
        while j - 1 >= 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1
            yield list(arr), {(j, "indianred"), (j-1, "indianred")}
        sorted_size += 1

def quickSort(arr: list[int]):
    # Pivot - Blue Color
    # i - darkorange
    # j - dark golden
    def _qs(arr, start=0, end=len(arr)-1):
        if start > end: return
        pivot = arr[start]
        i, j = start, end
        yield list(arr), [(i, "darkorange"), (j, "gold1")]
        while i < j:
            while i < len(arr) and arr[i] <= pivot:
                i+=1
                yield list(arr), [(start, "blue"), (i, "darkorange"), (j, "gold1")]
            while arr[j] > pivot :
                j-=1
                yield list(arr), [(start, "blue"), (i, "darkorange"), (j, "gold1")]
            if i < j:
                yield list(arr), [(i, "indianred"), (j, "indianred"), (start, "blue")]
                arr[i], arr[j] = arr[j], arr[i]
                yield list(arr), [(i, "indianred"), (j, "indianred"), (start, "blue")]
            else:
                yield list(arr), [(start, "blue"), (i, "darkorange"), (j, "gold1")]
        yield list(arr), [(start, "indianred"), (j, "indianred")]
        arr[j], arr[start] = arr[start], arr[j]
        yield list(arr), [(j, "blue"), (start, "indianred")]
        yield from _qs(arr, start, j-1)
        yield from _qs(arr, j+1, end)
    return _qs(arr)
