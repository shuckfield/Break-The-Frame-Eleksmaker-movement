# Break the Frame software

This is a simple script to home the Eleksmaker and then loop continually sending the gcode.

## Setup

1. Install [gcodesender](https://github.com/panzergame/gcodesender) - `git clone https://github.com/panzergame/gcodesender.git`
1. Install the requirements for gcodesender:
   1. `cd gcodesender`
   1. `pip3 install -r requirements.txt`
1. Set the Break the Frame GCode sender to start automatically
   1. `sudo cp break-thhe-frame.service /etc/systemd/system/`
   1. `sudo systemctl enable break-the-frame.service`
   1. `sudo service break-the-frame start`

