import time

import gcodesender.src.gcodesender.grbl

print("Let's go!")
s = gcodesender.src.gcodesender.grbl.Serial('/dev/ttyUSB0', 115200)

# Give it a moment or two to reset
time.sleep(2)

print("Homing")
print(s.send_wait_command("$H"))

# Uncomment this if you need to set the co-ordinate positions, but
# as it's written to EEPROM it's not necessary (or a good idea) to do it every time
#s.send_wait_command(s, b'G10 L2 P1 X-370Y-250')

# Move to the front left corner, as that's the origin we want gcodesender to use
s.send_wait_command('G0 X0Y0')

# GRBL tends to stop if you close the serial port mid-move, so give it some time to get there
time.sleep(10)

g = gcodesender.src.gcodesender.grbl.Controller(s)

print("Roll thhe tape!")
while True:
    g.send_file('/boot/movement.gcode')
    time.sleep(5)

