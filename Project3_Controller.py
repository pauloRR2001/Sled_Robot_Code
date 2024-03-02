# Basic remote control from microbit V1
# Trace the code to determine how the basic system works
# What would would a better interface for a different context?

from microbit import *
import radio

chnl = 19 #change the channel to your team number
radio.config(channel=chnl)
radio.on()

while True:
    #y = accelerometer.get_y() 
    a = button_a.is_pressed()
    b = button_b.is_pressed()
    if a:
        #forward
        display.show(Image.ARROW_W)
        radio.send("N")
    elif b:
        #back
        display.show(Image.ARROW_E)
        radio.send("S")
    else:
        continue
    sleep(10)