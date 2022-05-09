# Break the Frame

Files and code for the Break the Frame Eleksmaker

## Generating GCode

Once you've generated a Gcode file, copy it to the file names `movement.gcode` on the micro-SD card for the Raspberry Pi.  That will automatically get picked up and used by the [`loop-gcode.py`](software/loop-gcode.py) script when the system starts up.

The bed is 370mm by 250mm, so the gcode needs to fit into that area.  It's best to leave a 10mm margin round the edges too, so the machine won't hit the edge and go into the alarm state (which it'll mostly show by just stopping moving)

### Inkscape

1. Load the file in Inkscape, check the sizes in px (by default 1px = 1mm)
1. Choose `Extensions` -> `Gcodetools` -> `Tools library...` from the menu
1. Click `Apply` to generate the default tool
1. Change any of the relevant parameters by double (or maybe triple)-clicking on them.  The `feed` is the most obvious to change.  Something in the 2000-3000 range would be good for that, otherwise it wil be very slow moving around.
1. Choose `Extensions` -> `Gcodetools` -> `Path to Gcode...` from the menu
1. Switch to the `Preferences` tab
1. Set the filename you want to save to
1. Set the `Z safe height for G00 move over blank` to 0
1. Switch back to th `Path to Gcode` tab
1. Click `Apply` to generate the Gcode
1. Open the Gcode file in a text editor and remove the lines with `%` on them at the start and end of the file

### Other options

* [Kirimoto](https://grid.space/kiri/)
* [JScut.org](http://jscut.org/)

## Example GCode Files

There are a couple of example GCode files here:

* [example-bow-tie.gcode](example-bow-tie.gcode) — super-simple four-point "bow tie" shape
* [example-hammer-and-sickle.gcode](example-hammer-and-sickle.gcode) — hammer and sickle shape, generated with Inkscape

Copy any of them to `movement.gcode` to try them out.
