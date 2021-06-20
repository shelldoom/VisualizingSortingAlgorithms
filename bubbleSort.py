from random import choices, sample
from p5 import *

def arrayToGraph(arr: list[int], index: int = None):
    width = screen_width / len(arr)
    max_size = max(arr)
    # 1.05 because so that the bar is slightly below the top of the screen
    height_scale_factor = (screen_height//1.05) / max_size
    
    x = 0
    for i in range(len(arr)):
        stroke(0, 0, 50)
        stroke_weight(2)
        current_height = height_scale_factor * arr[i]
        fill(255, 165, 0)
        if index is not None and ((i == index) or (i < len(arr) - 1 and i == index + 1)):
            fill(179, 0, 0) # fill(0, 200, 32)
        rect(x, screen_height - current_height, width, current_height)
        x += width


def bubbleSortSteps(arr: list[int]):
    yield list(arr), 0
    n = len(arr)
    unsorted_length = n
    while unsorted_length > 0:
        for i in range(unsorted_length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            yield list(arr), i
        unsorted_length -= 1


screen_width, screen_height = 800, 600
input_arr = sample([i for i in range(1, 11)], 10)

result = None
iterator = None
index = 0
def setup():
    global iterator
    size(screen_width, screen_height)
    background(0)
    iterator = bubbleSortSteps(input_arr)
    result = next(iterator)
    arrayToGraph(result[0], 0)
    print("--"*5, input_arr, "--"*5)

r = None
def draw():
    global index, r
    background(0)
    try:
        r = next(iterator)
        arrayToGraph(r[0], r[1])
    except StopIteration:
        arrayToGraph(r[0], None)

if __name__ == "__main__":
    run(frame_rate=10)