from typing import TypeVar
import pygame
import sys
import random
from dataclasses import dataclass
from helper import *
import math

color = TypeVar('color', str, tuple[int])

@dataclass
class Point:
    x: int
    y: int

pygame.init()

# Avoid reducing the FPS, instead change the delay_seconds rather
# NOTE: Press `ENTER` many times to start sorting if the FPS is very low,
# since it becomes difficult to capture key/mouse events for lower FPS
FPS = 60
# Delay between each step
delay_seconds = 0.2
size = resX, resY = 800, 600
origin = Point(0, 0)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("SortingLyf")
clock = pygame.time.Clock()
zoom_factor = 1.03 # + (0.1 if FPS <= 15 else 0) + (0.1 if FPS <= 5 else 0)
zoom_offset = 15
translation_offset = 20 # + (5 if FPS <= 15 else 0) + (5 if FPS <= 5 else 0)

def displayArray(arr: list[int], beingUsed: set[tuple[int, color]], display_text: bool = True):
    smallest = min(arr)

    # How to deal with arrays whose length will result in going out of screen? 
    # Possible Solution: We merge few elements into one element
    # if len(arr) > resX:
    #     mergeSize = math.ceil(len(arr)/resX)
    #     arr = [
    #         sum(arr[i:i+mergeSize])/mergeSize 
    #         for i in range(0, len(arr), mergeSize)
    #     ]

    w = resX//len(arr)
    if w == 0: w = 1

    font = pygame.font.SysFont(None, w-5 if len(arr) > 10 else 40)
    scaling_factor = resY/(1.1*max(arr))
    maxHeight = resY

    if smallest < 0:
        scaling_factor = (resY/2)/(1.25*max(max(arr), -smallest))
        maxHeight = resY/2

    x = origin.x
    numbers_text = []
    bar_width = w-1 if w > 1 else w
    
    for index, value in enumerate(arr):
        # Default bar color
        bar_color = "darkolivegreen4"

        for i, color in beingUsed:
            if i == index:
                bar_color = color
                break
        bar_height = scaling_factor * value
        text = font.render(f"{value}", True, (255, 255, 255))

        if value >= 0:
            y = origin.y + maxHeight - bar_height
            pygame.draw.rect(screen, bar_color , pygame.Rect((x, y, bar_width, abs(bar_height))))
            if display_text: numbers_text.append((text, text.get_rect(center=(x+w/2, y-text.get_height()/2))))
        else:
            y = origin.y + resY/2
            pygame.draw.rect(screen, bar_color, pygame.Rect((x, y, bar_width, abs(bar_height))))
            if display_text: numbers_text.append((text, text.get_rect(center=(x+w/2, y + abs(bar_height) + text.get_height()/2))))
        x += w

    # Number text is drawn over
    if display_text:
        for number_text in numbers_text:
            screen.blit(number_text[0], number_text[1])


# Array Setup
arr = random.choices(range(-100, 100), k=30)
# List of columns/bars that are being compared/used while sorting algorithm is being executed
beingUsed = {} 
start_sorting = False
sorter = bubbleSort(arr)

while 1:
    scroll = 0
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4:
                scroll = 1
            if event.button == 5:
                scroll = -1

    # Start sorting the array?
    if pygame.key.get_pressed()[pygame.K_RETURN]:
        start_sorting = True
    
    screen.fill(0)

    # Display the array
    displayArray(arr, beingUsed, True)
    # Update the array by getting its next state
    if start_sorting:
        try:
            arr, beingUsed = next(sorter)
            pygame.time.delay(int(delay_seconds * 1000))
        except StopIteration:
            beingUsed = {}

    mouseX, mouseY = pygame.mouse.get_pos()

    # Zoom in/out the visualization 
    if pygame.key.get_pressed()[pygame.K_e] or scroll == 1:
        # Zoom in
        resX = int(resX * zoom_factor)
        resY = int(resY * zoom_factor)
        origin.x /= zoom_factor
        origin.y /= zoom_factor


    if pygame.key.get_pressed()[pygame.K_q] or scroll == -1:
        # Zoom out
        resX = int(resX / zoom_factor)
        resY = int(resY / zoom_factor)
        origin.x *= zoom_factor
        origin.y *= zoom_factor

    # Translate the visualization
    if pygame.key.get_pressed()[pygame.K_w] or pygame.key.get_pressed()[pygame.K_UP]:
        # Move Down
        origin.y = origin.y + translation_offset
    if pygame.key.get_pressed()[pygame.K_s] or pygame.key.get_pressed()[pygame.K_DOWN]:
        # Move Up
        origin.y = origin.y - translation_offset
    if pygame.key.get_pressed()[pygame.K_a] or pygame.key.get_pressed()[pygame.K_LEFT]:
        # Move left
        origin.x = origin.x + translation_offset
    if pygame.key.get_pressed()[pygame.K_d] or pygame.key.get_pressed()[pygame.K_RIGHT]:
        # Move Right
        origin.x = origin.x - translation_offset


