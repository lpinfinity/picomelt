from SendFrame import transmit_frame
import time

def arm_esc(pin):
    loop = 0
    while(loop < 2000):
        transmit_frame(str(0000000000000000), pin)
        time.sleep(.001)
        loop = loop + 1