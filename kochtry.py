#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 11:55:25 2024

@author: davidgordon
"""


stitches = [128, 2, 0, 0, 206, 206,]

def koch_snowflake_displacements(order, size, angle_offset=0, current_pos=(0, 0)):
    displacements = []

    def koch_snowflake(order, size, angle_offset=0):
        nonlocal current_pos, displacements

        if order == 0:
            # Record the displacement from the previous position
            displacements.append(current_pos)
            # Calculate the new position after the forward movement
            current_pos = (
                current_pos[0] + size * math.cos(math.radians(angle_offset)),
                current_pos[1] + size * math.sin(math.radians(angle_offset))
            )
            # Record the new position
            displacements.append(current_pos)
        else:
            for angle in [60, -120, 60, 0]:
                koch_snowflake(order - 1, size / 3, angle_offset + angle)

    import math

    for _ in range(3):
        koch_snowflake(order, size)
        angle_offset -= 120

    return displacements

# Set the order and size of the Koch snowflake
order = 3
size = 100

# Get the displacements of the Koch snowflake
snowflake_displacements = koch_snowflake_displacements(order, size)


# Print the displacements
for pos in snowflake_displacements:
    stitches += [0,0]
    stitches += [pos[0], pos[1]]
    
print(stitches)
    

for i in range(len(stitches)):
    if stitches[i] > 0:
        stitches[i] = int(stitches[i])
    elif stitches[i] < 0:
        stitches[i] = int(stitches[i])
        stitches[i] = 255 + stitches[i]
    else:
        stitches[i] = 0
        
stitches +=  [128, 16] 

print(stitches)

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


f.close()