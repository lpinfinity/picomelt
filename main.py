from machine import Pin
from machine import ADC
import time
from FrameCalculator import calcframe
from SendFrame import transmit_frame

pot = ADC(28)

loop = 0
# Init ESC
while loop < 2000:
    transmit_frame(str(0000000000000000), 0)
    transmit_frame(str(0000000000000000), 1)
    # transmit_frame(calcframe(0))
    # print(calcframe(0))
    loop = loop + 1
    time.sleep(.001)

while True:
    value = int(((pot.read_u16() / 65535) * 2000) + 47)
    print(calcframe(value))
    transmit_frame(calcframe(value), 0)
    transmit_frame(calcframe(value), 1)
    # transmit_frame(str(1000001011000110))
    # time.sleep(.001)
