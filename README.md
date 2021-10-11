## Visualizing Sorting Algorithms

![Insertion Sort Example](https://i.imgur.com/eDMQCpI.gif)
<p style="text-align: center;"><b>Insertion Sort</b></p>

### Control:
- Use `WASD` or `arrow` keys to move around
- Use `Q`, `E` or `mouse scroll` to zoom in/out (Not perfect, can't figure how to deal with this)
- Press `Enter` to start the sorting

**NOTE:** If the FPS set is very low, you might have to press `ENTER` many times to begin sorting

### Features:
- Supports negative numbers
- `Red` bar indicates there is swapping taking place
- `Yellow` bar indicates smaller pointer
- `Dark Yellow` bar indicates larger pointer
- For Quick Sort, `Blue` bar indicates the Pivot

### Implemented so far:
1. Insertion Sort
2. Bubble Sort
3. Quick Sort


### Todo List:
- Merge Sort, Radix Sort, Heap Sort, Shell Sort
- How to deal when the array size is so large that it can't fit in the screen
    - Reduce the array such that it autofits to the screen
    - Autofit to the screen while zooming in/out

### Requirements:
- Python 3.9 or above
- [pygame](pygame.org)

### Installation:
```bash
git clone <repository_url>.git
pip install -r requirements.txt
python3 ./main.py
```