# picomelt
A very unfinished project for a meltybrain spinner (combat robot) in micropython for the RP2040 using bidirectional Dshot.

Currently working:
- 
- Checksum calculations.
- Single directional Dshot up to Dshot 1200
- Multiple ESCs can be controlled independently.

Not working:
-
- Ability to read frames sent from the ESC.
- Anything regarding the accelerometer (H3LIS331DL)
- Communication with the transmitter (NRF24L01+)
- The part where it melts.
- Bidirectional Dshot is not currently implemented. I have tried to get it to work, but I am not sure if my ESCs support it/
