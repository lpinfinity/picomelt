from machine import Pin
from rp2 import PIO, StateMachine, asm_pio
import time
import machine

internal_pin = 0

machine.freq(270000000)

@asm_pio(sideset_init=PIO.OUT_LOW, out_shiftdir=PIO.SHIFT_LEFT)
def program():
    pull(block)
    set(y, 15)
    label('loop')
    out(x, 1)            .side(0)
    jmp(not_x, 'zero')   .side(1) [1]
    jmp('endloop')       .side(1) [1]
    label('zero')
    nop()                .side(0) [1]
    label('endloop')
    jmp(y_dec, 'loop')   .side(0)

# sm = StateMachine(0, program, freq=3600000, sideset_base=Pin(0)) #3600000
# sm.active(1)

def transmit_frame(frame: str, pin):
    # global internal_pin
    # internal_pin = pin
    sm = StateMachine(0, program, freq=3600000, sideset_base=Pin(pin))
    sm.active(1)
    sm.put(int(frame, 2), 16)

# transmit_frame('1000001011000110', 0)
# print(internal_pin)
# while True:
#     transmit_frame('1000001011000110')  # update with any value you like
    # time.sleep(.0001)



#0000000000000000
#1000001011000110
#111110100001010
#0000000000100010
    
#000000000010
#000000000000
#000000000010
#001000000000
#001000000010
#000000000010