#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 16:34:02 2024

@author: davidgordon
"""
#Laser Cut Box Project #1
#Max Plavcan
#David Gordon

#Outline
#Input Parameters
    #1. Box Dimensions (l x w x h)
    #2. Material Thickness

#Output
    #SVG code of custom Box

#import Python Numpy to aid in array operations
import numpy as np
import math

#Code for Input Criteria    
        
def getinputs():
    while True:
        try:
            
            length = float(input("Enter the Length in mm: "))
            if length < 50:
                print("Length inputed is too small. Please Try Again")
                continue
            
            width = float(input("Enter the Width in mm: "))
            if width < 50:
                print("Width inputed is too small. Please Try Again")
                continue
            height = float(input("Enter the Height in mm: "))
            if height < 40:
                print("Height inputed is too small. Please Try Again")
                continue
            
            #calculating maximum allowable dimesions so box fits on a page
            wmax = 2*length + 30
            hmax = 2*height + 40
        
            if not (0 <= wmax <= 275) or not  (0 <= hmax <= 212):
                print("Error: Input values out of range")
                continue
            
            #limiting fractal input since its computationally intense
            order_input = int(input("Enter your Fractal Order for Pattern #1 (Please keep input under 8): "))
            if order_input > 8:
                print("Order input is too high. Please Try Again")
                continue
            
            frac1_iter = int(input("Enter the Total Number of Fractal Interations for Pattern #2: "))
            if frac1_iter > 50:
                print("Fractal Interations input is too high. Please Try Again")
                continue
            
            textfront = input("Enter your UNI: ")
            if len(textfront) > 10:
                print("Error: UNI is too long. Try again")
                continue 
            
            texttop  = input("Enter your First Name: ")
            if len(texttop) > 14:
                print("You've reach the maximum amount of characters. Please Try Again")
                continue
        
            
            return texttop, textfront, length, width, height, order_input, frac1_iter

        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")

texttop, textfront, length, width, height, order_input, frac1_iter = getinputs()        

#Code to Generate SVG file for Box

f = open("boxfile.svg", "w") #Creates and Opens an svg file and enables write privileges
f.write(f'<?xml version=\"1.0\" encoding=\"UTF-8\" ?> \n') #Initiates svg format
f.write(f'<svg xmlns=\"http://www.w3.org/2000/svg\" version=\"1.1\"> \n') #Loads software

###Box Properties###
#Fastener Properties
fast_dia = 0.086 * 25.4 #Fastener diameter
fast_r = fast_dia/2 #Fastener radius
fast_length = 0.375 * 25.4 #Fastener length
nut_width = .188 * 25.4 # Nut width
nut_thick = .063 * 25.4 #Nut thickness

#Material Properties
mat_thick = .125 * 25.4 #Cardboard Thickness

#Margins of Box Outline
w_marg = 10 #width margin
h_marg = 10 #height margin
l_marg = 10 #length margin

#Positioning of Box Faces
BL = np.zeros((6,2)) #Matrix with all values
#First Row
#Face 1 (w x h)
BL[0,0], BL[0,1] = width/2 + w_marg, height/2 + h_marg
#Face 2 (w x h)
BL[1,0], BL[1,1] = BL[0,0] + width + w_marg, BL[0,1]

#Second Row
#Face 5 (TOP) (l x w)
BL[4,0], BL[4,1] = length/2 + l_marg, BL[0,1] + height/2 + width/2 + w_marg
#Face 6 (BOTTOM) (1 x w)
BL[5,0], BL[5,1] = BL[4,0] + length + l_marg, BL[4,1]

#Third Row
#Face 3 (l x h)
BL[2,0], BL[2,1] = length/2 + l_marg, BL[4,1] + width/2 + height/2  + h_marg
#Face 4 (l x h)
BL[3,0], BL[3,1] = BL[2,0] + length + l_marg , BL[4,1] + width/2 + height/2  + h_marg

#Box Face - Type I (Circumferential) (Qty:4) (faces using Width, Height and Length)
def boxface_t1(x_t1, y_t1, L1, L2): 
    #Inputs are x location and y location, L1 (Width or Length) and L2 (Height)
    #Output is svg code that geometrically represents a box face
    #Quadrant 1 (upper left)
    P_t1 = np.zeros((15, 2)) #Array of points that define 1 quadrant of a face
    P_t1[0,0], P_t1[0,1] = x_t1 - (L1/2), y_t1
    P_t1[1,0], P_t1[1,1] = P_t1[0,0], P_t1[0,1] - (((L2/2)-mat_thick)/3)
    P_t1[2,0], P_t1[2,1] = P_t1[1,0] + mat_thick, P_t1[1,1]
    P_t1[3,0], P_t1[3,1] = P_t1[2,0], P_t1[2,1] - (((L2/2)-mat_thick)/3)
    P_t1[4,0], P_t1[4,1] = P_t1[3,0] - mat_thick, P_t1[3,1]
    P_t1[5,0], P_t1[5,1] = P_t1[4,0], P_t1[4,1] - (((L2/2)-mat_thick)/3)
    P_t1[6,0], P_t1[6,1] = P_t1[5,0] + ((L1/2)-(fast_dia/2))/3, P_t1[5,1]
    P_t1[7,0], P_t1[7,1] = P_t1[6,0], P_t1[6,1] - mat_thick
    P_t1[8,0], P_t1[8,1] = P_t1[7,0] + ((L1/2)-(fast_dia/2))/3, P_t1[7,1]
    P_t1[9,0], P_t1[9,1] = P_t1[8,0], P_t1[8,1] + mat_thick
    P_t1[10,0], P_t1[10,1] = P_t1[9,0] + ((L1/2)-(fast_dia/2))/3, P_t1[9,1]
    P_t1[11,0], P_t1[11,1] = P_t1[10,0], P_t1[10,1] + (fast_length-mat_thick-nut_thick)
    P_t1[12,0], P_t1[12,1] = P_t1[11,0] - ((nut_width/2)-(fast_dia/2)), P_t1[11,1]
    P_t1[13,0], P_t1[13,1] = P_t1[12,0], P_t1[12,1] + nut_thick
    P_t1[14,0], P_t1[14,1] = P_t1[13,0] + (nut_width/2), P_t1[13,1]
    
    #Quadrant 2 (lower left)
    P_t1_q2 = np.zeros((15, 2)) #Array of points that define 2 quadrant of a face
    for i in range(len(P_t1)):
        P_t1_q2[i,0] = P_t1[i,0]
        P_t1_q2[i,1] = P_t1[i,1] + 2 * abs(y_t1 - P_t1[i,1])

    #Quadrant 3 (upper right)
    P_t1_q3 = np.zeros((15, 2)) #Array of points that define 3 quadrant of a face
    P_t1_q3[0,0], P_t1_q3[0,1] = x_t1 + (L1/2) - mat_thick, y_t1
    P_t1_q3[1,0], P_t1_q3[1,1] = P_t1_q3[0,0], P_t1_q3[0,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[2,0], P_t1_q3[2,1] = P_t1_q3[1,0] + mat_thick, P_t1_q3[1,1]
    P_t1_q3[3,0], P_t1_q3[3,1] = P_t1_q3[2,0], P_t1_q3[2,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[4,0], P_t1_q3[4,1] = P_t1_q3[3,0] - mat_thick, P_t1_q3[3,1]
    P_t1_q3[5,0], P_t1_q3[5,1] = P_t1_q3[4,0], P_t1_q3[4,1] - (((L2/2)-mat_thick)/3)
    P_t1_q3[6,0], P_t1_q3[6,1] = P_t1_q3[5,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[5,1]
    P_t1_q3[7,0], P_t1_q3[7,1] = P_t1_q3[6,0], P_t1_q3[6,1] - mat_thick
    P_t1_q3[8,0], P_t1_q3[8,1] = P_t1_q3[7,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[7,1]
    P_t1_q3[9,0], P_t1_q3[9,1] = P_t1_q3[8,0], P_t1_q3[8,1] + mat_thick
    P_t1_q3[10,0], P_t1_q3[10,1] = P_t1_q3[9,0] - ((L1/2)-(fast_dia/2)-mat_thick)/3, P_t1_q3[9,1]
    P_t1_q3[11,0], P_t1_q3[11,1] = P_t1_q3[10,0], P_t1_q3[10,1] + (fast_length-mat_thick-nut_thick)
    P_t1_q3[12,0], P_t1_q3[12,1] = P_t1_q3[11,0] + ((nut_width/2)-(fast_dia/2)), P_t1_q3[11,1]
    P_t1_q3[13,0], P_t1_q3[13,1] = P_t1_q3[12,0], P_t1_q3[12,1] + nut_thick
    P_t1_q3[14,0], P_t1_q3[14,1] = P_t1_q3[13,0] - (nut_width/2), P_t1_q3[13,1]

    #Quadrant 4 (bottom right)
    P_t1_q4 = np.zeros((15, 2)) #Array of points that define 4 quadrant of a face
    for i in range(len(P_t1_q4)):
        P_t1_q4[i,0] = P_t1_q3[i,0]
        P_t1_q4[i,1] = P_t1_q3[i,1] + 2 * abs(y_t1 - P_t1_q3[i,1])

    #Combine all quadrants
    P_t1_reshape = ' '.join([f"{', '.join(map(str, row))}" for row in P_t1])
    P_t1_q2_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q2]))
    P_t1_q3_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q3]))
    P_t1_q4_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t1_q4]))

    q1 = f'   <polyline points="{P_t1_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q2 = f'   <polyline points="{P_t1_q2_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q3 = f'   <polyline points="{P_t1_q3_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q4 = f'   <polyline points="{P_t1_q4_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    return q1+q2+q3+q4

#Box Face - Type II (Top & Bottom faces) (Qty:2) (faces using Width and Length)
def boxface_t2(x_t2, y_t2): 
    #Inputs are x location and y location
    #Output is svg code that geometrically represents a box face
    
    #Quadrant 1 (upper left)
    P_t2_q1 = np.zeros((11, 2)) #Array of points that define 1 quadrant of a face

    P_t2_q1[0,0], P_t2_q1[0,1] = x_t2 - (length/2), y_t2
    P_t2_q1[1,0], P_t2_q1[1,1] = P_t2_q1[0,0], P_t2_q1[0,1] - width/6
    P_t2_q1[2,0], P_t2_q1[2,1] = P_t2_q1[1,0] + mat_thick, P_t2_q1[1,1]
    P_t2_q1[3,0], P_t2_q1[3,1] = P_t2_q1[2,0], P_t2_q1[2,1] - width/6
    P_t2_q1[4,0], P_t2_q1[4,1] = P_t2_q1[3,0] - mat_thick, P_t2_q1[3,1]
    P_t2_q1[5,0], P_t2_q1[5,1] = P_t2_q1[4,0], P_t2_q1[4,1] - width/6
    P_t2_q1[6,0], P_t2_q1[6,1] = P_t2_q1[5,0] + (length/6), P_t2_q1[5,1]
    P_t2_q1[7,0], P_t2_q1[7,1] = P_t2_q1[6,0], P_t2_q1[6,1] + mat_thick
    P_t2_q1[8,0], P_t2_q1[8,1] = P_t2_q1[7,0] + (length/6), P_t2_q1[7,1]
    P_t2_q1[9,0], P_t2_q1[9,1] = P_t2_q1[8,0], P_t2_q1[8,1] - mat_thick
    P_t2_q1[10,0], P_t2_q1[10,1] = P_t2_q1[9,0] + (length/6), P_t2_q1[9,1]
    
    #Quadrant 2 (bottom left)
    P_t2_q2 = np.zeros((11, 2)) #Array of points that define a quadrant face
    for i in range(len(P_t2_q1)):
        P_t2_q2[i,0] = P_t2_q1[i,0]
        P_t2_q2[i,1] = P_t2_q1[i,1] + 2 * abs(y_t2 - P_t2_q1[i,1])
    
    #Quadrant 3 (upper right)
    P_t2_q3 = np.zeros((11, 2)) #Array of points that define a quadrant face
    P_t2_q3[0,0], P_t2_q3[0,1] = x_t2 + (length/2), y_t2
    P_t2_q3[1,0], P_t2_q3[1,1] = P_t2_q3[0,0], P_t2_q3[0,1] - width/6
    P_t2_q3[2,0], P_t2_q3[2,1] = P_t2_q3[1,0] - mat_thick, P_t2_q3[1,1]
    P_t2_q3[3,0], P_t2_q3[3,1] = P_t2_q3[2,0], P_t2_q3[2,1] - width/6
    P_t2_q3[4,0], P_t2_q3[4,1] = P_t2_q3[3,0] + mat_thick, P_t2_q3[3,1]
    P_t2_q3[5,0], P_t2_q3[5,1] = P_t2_q3[4,0], P_t2_q3[4,1] - width/6
    P_t2_q3[6,0], P_t2_q3[6,1] = P_t2_q3[5,0] - (length/6), P_t2_q3[5,1]
    P_t2_q3[7,0], P_t2_q3[7,1] = P_t2_q3[6,0], P_t2_q3[6,1] + mat_thick
    P_t2_q3[8,0], P_t2_q3[8,1] = P_t2_q3[7,0] - (length/6), P_t2_q3[7,1]
    P_t2_q3[9,0], P_t2_q3[9,1] = P_t2_q3[8,0], P_t2_q3[8,1] - mat_thick
    P_t2_q3[10,0], P_t2_q3[10,1] = P_t2_q3[9,0] - (length/6), P_t2_q3[9,1]

    #Quadrant 4 (bottom right)
    P_t2_q4 = np.zeros((11, 2)) #Array of points that define a quadrant face
    for i in range(len(P_t2_q3)):
        P_t2_q4[i,0] = P_t2_q3[i,0]
        P_t2_q4[i,1] = P_t2_q3[i,1] + 2 * abs(y_t2 - P_t2_q3[i,1])

    #Hole Locations
    HL = np.zeros((4,2)) #Matrix with all hole locations
    EM = mat_thick/2 #Edge Margin of fastener hole to material edge 9this ensures holes are centered on material thickness
    HL[0,0], HL[0,1] = x_t2 - (length/2) + EM, y_t2
    HL[1,0], HL[1,1] = x_t2, y_t2 - (width/2) + EM
    HL[2,0], HL[2,1] = x_t2 + (length/2) - EM, y_t2
    HL[3,0], HL[3,1] = x_t2, y_t2 + (width/2) - EM
    
    #Combine all quadrants
    P_t2_q1_reshape = ' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q1])
    P_t2_q2_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q2]))
    P_t2_q3_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q3]))
    P_t2_q4_reshape = (' '.join([f"{', '.join(map(str, row))}" for row in P_t2_q4]))
    
    q1_2 = f'   <polyline points="{P_t2_q1_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q2_2 = f'   <polyline points="{P_t2_q2_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q3_2 = f'   <polyline points="{P_t2_q3_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    q4_2 = f'   <polyline points="{P_t2_q4_reshape}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc1 = f'   <circle cx="{HL[0,0]}" cy="{HL[0,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc2 = f'   <circle cx="{HL[1,0]}" cy="{HL[1,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc3 = f'   <circle cx="{HL[2,0]}" cy="{HL[2,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'
    Hole_loc4 = f'   <circle cx="{HL[3,0]}" cy="{HL[3,1]}" r="{fast_r}" stroke="black" stroke-width="1" fill="none" /> \n'

    return q1_2+q2_2+q3_2+q4_2+Hole_loc1+Hole_loc2+Hole_loc3+Hole_loc4

#Drawing Each Box Face
#Face 1,2,3,4
f.write(boxface_t1(BL[0,0], BL[0,1], width, height ))
f.write(boxface_t1(BL[1,0], BL[1,1], width, height))
f.write(boxface_t1(BL[2,0], BL[2,1], length, height))
f.write(boxface_t1(BL[3,0], BL[3,1], length, height))
#Face  5 & 6 (Top and Bottom)
f.write(boxface_t2(BL[4,0], BL[4,1]))
f.write(boxface_t2(BL[5,0], BL[5,1]))


#coordinates for cu logo and input text
xculogo = BL[2,0] - length/8
xcusz = .2*length
ycusz = .2*height
yculogo = BL[2,1] - height/8
dmx = l_marg + mat_thick + 2
dmy = 3*h_marg + height + width + mat_thick + 5.5
uniy = dmy + 5


#adjusting digital manufacturing font size so it fits in the front
if length < 60:
    dmfontsize = 2.5
elif 60 <= length < 75 or height < 50:
    dmfontsize = 3
else:
    dmfontsize = 5

#adjusting the name font size so it fits on the top
if length < 65:
    namefont = 4
elif 65 <= length <= 100:
    namefont = 5
else:
    namefont = 8
    

f.write(f'<text x="{dmx}" y="{dmy}" font-family="Brush Script MT" font-size="{dmfontsize}" font-weight="bold" fill="red">{textfront}</text>\n')
f.write(f'<image href="/Users/davidgordon/Documents/Python DM/CUlogored.png" x="{xculogo}" y="{yculogo}" width="{xcusz}" height="{ycusz}" />\n')
f.write(f'<text x="{dmx}" y="{uniy}" font-family="Brush Script MT" font-size="{dmfontsize}" font-weight="bold" fill="red">Digital Manufacturing</text>\n')


#coordinates for name writing on top
xname = dmx
yname = 2*h_marg + height + 15
texttop = texttop + "'s"
ybox = yname + 10
f.write(f'<text x="{xname}" y="{yname}" font-family="Comic Sans MS" font-size="{namefont}" font-weight="bold" fill="red">{texttop}</text>\n')
f.write(f'<text x="{xname}" y="{ybox}" font-family="Comic Sans MS" font-size="{namefont}" font-weight="bold" fill="red">box</text>\n')


#snowflake pattern

def snowflake(center_x, center_y, order):
    def snowflake_segment(x1, y1, x2, y2, order):
        if order == 0:
            return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="red" stroke-width=".25" />\n'
        
        # intermediate points
        x3 = (2 * x1 + x2) / 3
        y3 = (2 * y1 + y2) / 3
        x4 = (x1 + 2 * x2) / 3
        y4 = (y1 + 2 * y2) / 3

        # Tip of the pattern
        x5 = x3 + (x4 - x3) * math.cos(math.radians(60)) - (y4 - y3) * math.sin(math.radians(60))
        y5 = y3 + (x4 - x3) * math.sin(math.radians(60)) + (y4 - y3) * math.cos(math.radians(60))

        # generate each segment
        segment = snowflake_segment(x1, y1, x3, y3, order - 1)
        segment += snowflake_segment(x3, y3, x5, y5, order - 1)
        segment += snowflake_segment(x5, y5, x4, y4, order - 1)
        segment += snowflake_segment(x4, y4, x2, y2, order - 1)

        return segment

    # Calculate initial points of the pattern
    side_length = height/2.5 # size of pattern
    x1 = center_x - side_length / 2
    y1 = center_y - (side_length * math.sqrt(3) / 6)
    x2 = center_x + side_length / 2
    y2 = center_y - (side_length * math.sqrt(3) / 6)
    x3 = center_x
    y3 = center_y + (2 * side_length * math.sqrt(3) / 6)

    # generating text
    snowflake = snowflake_segment(x1, y1, x2, y2, order)
    snowflake += snowflake_segment(x2, y2, x3, y3, order)
    snowflake += snowflake_segment(x3, y3, x1, y1, order)

    return f'{snowflake}'

#postion coordinates for snowflake
x_tip_snow = BL[0,0]
y_tip_snow = BL[0,1]

f.write(snowflake(x_tip_snow, y_tip_snow, order_input))



#Factal Parameters For Pattern Number 1
frac_inc = (2*math.pi)/frac1_iter
frac_rad = 5 #Radius of circle used for fractal pattern
frac_marg = 10 #Edge margin for fractal pattern

#IF statment to understand what the critical edge dimension is
if width/2 <= (height/2 -fast_length):
    frac_rad_pos = width/2 - mat_thick - frac_rad - frac_marg
else:
    frac_rad_pos = height/2 - mat_thick - frac_rad - fast_length - frac_marg

#Initiate fractal pattern starting coordinates
frac_nx = BL[1,0] + frac_rad_pos
frac_ny = BL[1,1]


#Fractal pattern generator
for i in range(frac1_iter+1):
    f.write(f'<circle cx="{BL[1,0] - frac_nx}" cy="{BL[1,1] - frac_ny}" r="{frac_rad}" stroke="red" stroke-width=".5" fill="none" /> \n')
    frac_nx = frac_rad_pos * math.cos((frac_inc * i))
    frac_ny = frac_rad_pos * math.sin((frac_inc * i))

#Close code string
f.write(f'</svg>')
f.close()