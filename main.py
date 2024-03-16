from machine import Pin
from machine import ADC
import time
from FrameCalculator import calcframe
from SendFrame import transmit_frame
import DshotFunctions

#Used as control input for testing
pot = ADC(28)

DshotFunctions.arm_esc(0)
DshotFunctions.arm_esc(1)

while True:
    value = int(((pot.read_u16() / 65535) * 2000) + 47)
    print(calcframe(value))
    transmit_frame(calcframe(value), 0)
    transmit_frame(calcframe(value), 1)
    # transmit_frame(str(1000001011000110))
    # time.sleep(.001)
