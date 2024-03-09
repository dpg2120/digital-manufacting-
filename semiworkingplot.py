#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 11:20:59 2024

@author: davidgordon
"""
import matplotlib.pyplot as plt


def calculate_displacements(coordinates):
    displacements = []

    for i in range(0, len(coordinates)-4, 2):
        x1, y1 = coordinates[i], coordinates[i+1]
        x2, y2 = coordinates[i+2], coordinates[i+3]

        dx = round(x2 - x1)
        dy = round(y2 - y1)
        
        if dx > 0:
            dx = dx
        elif dx < 0:
            dx = 255 + dx
        else:
            dx = 0
        
        if dy > 0:
            dy = dy
        elif dy < 0:
            dy = 255 + dy
        else:
            dy = 0
        
        #displacements.extend([0,0])
        displacements.extend([0, 0, dx, dy])

    return displacements

def draw_fractal(x, y, order, size, coordinates=[]):
    if order == 0:
        # Draw the triangle
        coordinates.extend([x, y, x + size, y, x + size / 2, y + size * (3 ** 0.5) / 2])
    else:
        size /= 2

        # Recursive calls for the three sub-triangles
        draw_fractal(x, y, order - 1, size, coordinates)
        draw_fractal(x + size, y, order - 1, size, coordinates)
        draw_fractal(x + size / 2, y + size * (3 ** 0.5) / 2, order - 1, size, coordinates)



'''        
def draw_fractal(x, y, order, size, coordinates=[]):
    if order == 0:
        coordinates.extend([x, y])
    else:
        size /= 3

        draw_fractal(x, y, order - 1, size, coordinates)

        x += size
        y += 0
        draw_fractal(x, y, order - 1, size, coordinates)

        x += size * 0.5
        y += size * (3 ** 0.5 / 2)
        draw_fractal(x, y, order - 1, size, coordinates)

        x += size * 0.5
        y -= size * (3 ** 0.5 / 2)
        draw_fractal(x, y, order - 1, size, coordinates)

        x += size
        y += 0
        draw_fractal(x, y, order - 1, size, coordinates)    
  
def draw_fractal(x, y, order, size, coordinates=[]):
    if order == 0:
        coordinates.extend([x, y])
    else:
        size /= 3
        draw_fractal(x, y, order - 1, size, coordinates)
        x += size
        draw_fractal(x, y, order - 1, size, coordinates)
        x += size
        draw_fractal(x, y, order - 1, size, coordinates)
        x -= 2 * size
        y += size
        draw_fractal(x, y, order - 1, size, coordinates)
        x += size
        draw_fractal(x, y, order - 1, size, coordinates)
'''

def plot_coordinates(coordinates):
    x = coordinates[::2]  # Extract x-coordinates
    y = coordinates[1::2]  # Extract y-coordinates

    plt.plot(x, y, marker='o', linestyle='-', color='b')
    plt.title('Plot of Coordinates')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.grid(True)
    plt.show()



def main():
    global stitches
    global coordinates
    coordinates = []
    draw_fractal(0, 0, 3, 200, coordinates)  # Adjust the order and size as needed

    print(coordinates)
    ostitches = [128, 2, 0, 0, 206, 206,]

    displace = calculate_displacements(coordinates)
 
    stitches = ostitches + displace + [128, 16]
    print(stitches)
    
    plot_coordinates(coordinates)

 
    
    
    ###
    jefBytes = [124, 0, 0, 0,   # The byte offset of the first stitch
                10, 0, 0, 0,    # Unknown number
                ord("2"), ord("0"), ord("1"), ord("9"), # YYYY
                ord("0"), ord("2"), ord("2"), ord("4"), # MMDD
                ord("1"), ord("2"), ord("3"), ord("0"), # HHMM
                ord("0"), ord("0"), 99, 0,  # SS00
                1, 0, 0, 0,     # Number of physical threads (1)
                (len(stitches)//2) & 0xff, (len(stitches)//2) >> 8 & 0xff, 0, 0,     # Number of stitches
                3, 0, 0, 0,     # Sewing machine hoop             
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Left boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Top boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Right boundary distance from center (in 0.1 mm)
                50, 0, 0, 0,   # Bottom boundary distance from center (in 0.1 mm)
                2, 0, 0, 0,         # Thread color (white)
                13, 0, 0, 0,        # Unknown number
                ] + stitches
     
    
    jefBytes = bytes(jefBytes)
    with open("snow.jef", "wb") as f:
        f.write(jefBytes)


if __name__ == "__main__":
    main()