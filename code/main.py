from machine import ADC
from Dshot.SendFrame import transmit_frame
from Dshot import DshotFunctions
from Dshot.FrameCalculator import calcframe
import machine
import time

machine.freq(250000000)

#Used as control input for testing
pot = ADC(28)

DshotFunctions.arm_esc(0)
DshotFunctions.arm_esc(1)

while True:
    # value = int(((pot.read_u16() / 65535) * 2000) + 47)
    value = 100
    print(calcframe(value))
    transmit_frame(calcframe(value), 0)
    transmit_frame(calcframe(value), 1)
    # transmit_frame(str(1000001011001001), 1)
    # time.sleep(.001)
