from SendFrame import transmit_frame
from FrameCalculator import calcframe
import time

def arm_esc(pin):
    loop = 0
    while(loop < 2000):
        transmit_frame(str(0000000000000000), pin)
        time.sleep(.001)
        loop = loop + 1

def set_throttle(throttle, pin):
    transmit_frame(calcframe(throttle), pin)