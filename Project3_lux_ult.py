'''
===============================================================================
ENGR 130 Program Description 
	User defined function that reads and sends the signals from the infra red sensor

Assignment Information
	Assignment:     project 3, Team 19
	Author:         team 19
	Team ID:        19 
	

=+=============================================================================
'''

"""
------------------------------------
Name of function: lucent_singularity
Viarialbes:
        no input
Purpose: Checks if the input is an integer and outputs error if it is not 
Author: team 19
------------------------------------
"""

from microbit import *

#Infrared Sensor detection, returns light value
def lucent_singularity():
    light_level = pin1.read_analog() #Get light reading
    return light_level