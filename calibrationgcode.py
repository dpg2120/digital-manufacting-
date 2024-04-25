#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 08:36:17 2024

@author: davidgordon
"""

#gcode generator
#Group 18

#import Libraries
import numpy as np
import math

#Initiate Parameters
print("Please physically move extrusion head to 0,0,0 and reset syringe on CNC machine prior to print")

#Spirograph Pattern Parameters (User Preference, toggle as needed)
#minor Circles
r_circ = 10 #radius of each individual circle in spirograph pattern [mm]
circ_res = 15 #number of points used to costruct each minor circle
#Major Circle
n = 25 #total number of circles in pattern
r_tot = 25 #radius of entire pattern circle [mm]

#Machine Parameters (Intrinsic Properites, toggle as needed)
nzl_dia = 0.89 #mm diameter of extrusion nozzle, assumes 18 gauge [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_w = 254 #mm width (left to right) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]
bed_l = 254 #mm length (front to back) of print bed [EXPERIMENTAL PARAMETER, Toggle as Needed]

#Material Properties (EXPERIMENTAL)
#Material 1 (Hardening Syrup)

#f1 = float(input("Enter the feedrate of syrup [mm/s] range: ")) #Feedrate, originally 120 mm/min [EXPERIMENTAL PARAMETER, Toggle as Needed]
lay_h = float(input("Enter the layer height of syrup [mm]: ")) #layer height [EXPERIMENTAL PARAMETER, Toggle as Needed]
e_rate_1 = float(input("Enter the extrusion distance of syrup [mm]: ")) #Extrusion Distance, originally 2 mm extrusion of syringe for Material 1 [EXPERIMENTAL PARAMETER, Toggle as Needed]

#Define g code write function
def write_gcode(file, gcode_data):
    with open(file, 'w') as f:
        for command in gcode_data:
            f.write(command + '\n')

#Write g code data
#Initial Block
data = [";Group 18 gcode Generator", #Header text
        "G21", #Switch to metric units
        "G90", #Switch to absolute units
        "M106 S255", #Starts fan on printer
        "G92 X0 Y0 Z0 E0", #Set current extrusion head position to 0,0,0 and extrusion head to 0]] #moves extruder to next point
        "M83", #Extruder head set to relative mode
        ]

data += ["G0 X20 Y20 Z3"] #Extrude Step

x = 20
y = 20
z = lay_h
f1 = 110



#Varying Feedrate
for i in range(5):
    y = y + 30
    data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrude Step
    z += lay_h
    y = y - 30
    data += ["G1 X{} Y{} Z{} E{} F{}".format(x,y,z,e_rate_1, f1),] #Extrude Step
    y = y + 5
    data += ["G0 X{} Y{} Z{}".format(x,y,z),] #backtrack
    y = y - 5
    x = x + 10
    data += ["G0 X{} Y{} Z3".format(x,y),]
    f1 += 5
    z = lay_h

    


data += ["G0 X0 Y0 Z0",] #Return to origin after print
data += ["M106 S0"] #turn printer fan off

##################

#Generate gcode
write_gcode("Food_Print_Calibration_G18.gcode", data)