def calcframe(value):
    # Add telemetry bit to value
    value = f'{value:08b}'
    value = value + '0'
    value = int(value, 2)
    
    # Calculate CRC checksum
    # crc = (value ^ (value >> 4) ^ (value >> 8)) & 0x0F
    crc = ((value ^ (value >> 4) ^ (value >> 8))) & 0x0F
    
    # Add CRC to value
    frame = f'{value:08b}' + f'{crc:08b}'[4:]
    print(frame)
    
    return frame
    
# calcframe(1046)

# 1111111111101110