'''
===============================================================================
ENGR 130 Program Description 
	This function uses and syncronizes the rotor servos relative to the IR sensor's readings

Assignment Information
	Assignment:     Project 3
	Author:         Team 19
	Team ID:        19 (individual for this hw) 
	

=+=============================================================================
'''

from microbit import *
import lux_ult as root
import robotbit_library as r
# Define ports for the band of high current output S1-8
S1 = 0x1 # used for standard servo in this example
S2 = 0x2
S3 = 0x3
S4 = 0x4
S5 = 0x5
S6 = 0x6
S7 = 0x7
S8 = 0x8

r.setup()      # set up the robotbit


"""
------------------------------------
Name of function: see_snow
Viarialbes:
        sled_down, current position of the sled
Purpose: Processes the IR sensor's radings
Author: Team 19
------------------------------------
"""

def see_snow(sled_down): #uses strength of reflected light from IR sensor value to either movethe sled down or ligt it up
    light = root.lucent_singularity()
    if light <= 40: #40 was the value used to determine whether there was snow or not. If "light" is less than or equal than 40, then sled would be down. If not, sled is up
        if sled_down == False:
            sled_toggle()
            print('The sled is now down')
            sled_down = True
    elif light > 40:
        if sled_down == True:
            sled_toggle()
            print('The sled is now up')
            sled_down = False
    return sled_down

"""
------------------------------------
Name of function: sled_toggle
Viarialbes:
        no inputs
Purpose: controls the sled toggle through the servos independently from events
Author: team 19
------------------------------------
"""
def sled_toggle():
    r.servo(S1, 146.75) #Motion the servos to rotate
    r.servo(S3, 80.92) #This servo faces right, 180 - angle to ensure
    #that they rotate in the same direction
    sleep(445)
    r.servo(S1, 117) #Motion the servos to stop/personally calibrated
    r.servo(S3, 115)
    return 0