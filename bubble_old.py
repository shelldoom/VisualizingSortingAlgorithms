from random import choices, sample
from p5 import *

def arrayToGraph(arr: list[int], index: int = None):
    width = screen_width / len(arr)
    max_size = max(arr)
    height_scale_factor = (screen_height//1.05) / max_size
    
    x = 0
    for i in range(len(arr)):
        stroke(0, 0, 50)
        stroke_weight(2)
        current_height = height_scale_factor * arr[i]
        fill(255, 165, 0)
        # if (index and condition2):  
        # This was not done
        # Expected result is that it is false when 'index is None' 
        # But python makes the statement false even when index is 0
        if index is not None and (i == index or (i < len(arr) - 1 and i == index + 1)):
            fill(179, 0, 0)
        rect(x, screen_height - current_height, width, current_height)
        x += width


def bubbleSortSteps(arr: list[int]):
    result = [[list(arr), 0]]
    n = len(arr)
    unsorted_length = n
    while unsorted_length > 0:
        for i in range(unsorted_length - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
            result.append([list(arr), i])
        unsorted_length -= 1
    return result



screen_width, screen_height = 800, 600
input_arr = sample([i for i in range(1, 31)], 30)

result = None
index = 0
def setup():
    size(screen_width, screen_height)
    global result
    result = bubbleSortSteps(input_arr)
    background(0)
    arrayToGraph(result[0][0], 0)
    print("--"*20)
    print(input_arr)
    print("--"*20)
    print(result[-1])
    print("--"*20)


def draw():
    global index
    background(0)
    if index < len(result):
        cur = result[index]
        arrayToGraph(cur[0], cur[1])
        index += 1
    else:
        arrayToGraph(result[-1][0], None)
        index += 1
        if index > len(result) + 10:
            time.sleep(2)
            index = 0

# bubbleSort([10, 2, 3, 45, 1, -2])


if __name__ == "__main__":
    run(frame_rate=25)
