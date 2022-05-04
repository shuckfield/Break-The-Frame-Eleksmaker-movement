import serial
import time

def sendCommand(s, cmd):
    if s:
        s.write(cmd+b'\n')
        grbl_out = s.readline().strip()
        print(">>",cmd)
        print("out:",grbl_out)

s = serial.Serial('/dev/ttyUSB0', 115200, timeout=60)
# Give it a moment or two to reset
time.sleep(2)

up_clean = False
while not up_clean:
        # Reset GRBL
        print("sending reset")
        s.write(b"\x18\r\n\r\n")
        # Give it a moment or two to reset
        time.sleep(1)
        start = int(time.time())
        while not up_clean and time.time() < start + 10:
                l = s.readline().strip()
                print(">>",l)
                if l == b'ok':
                        # Things seem okay, so let's carry on
                        up_clean = True
                time.sleep(1)

s.flushInput()
sendCommand(s, b'$H')
sendCommand(s, b'G10 L2 P1 X-380Y-260')
# Move to the front left corner, as that's the origin we want gcodesender to use
sendCommand(s, B'G0 X0Y0')
