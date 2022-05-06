# Hardware Details

## Main Assembly

Main assembly is an Eleksmaker plotter.

## Limit Switches

### Parts

* 2 x [microswitch](https://uk.rs-online.com/web/p/microswitches/0515690/)
* 2 x 100nF (0.1uF or 104) capacitors
* 2 x 4k7ohm resistors
* 2 x t-nuts
* 2 x 2-way screw terminals
* 1 x 2x7 0.1" header socket
* A small 7x12 hole piece of veroboard

### Assembly

1. Locate the t-nuts into the outside channels of the extrusion for one side of the y-axis
1. Bolt one of the limit switches into the t-nuts
1. Using the [wiring diagram for the Eleksmaker controller](http://eleksmakeross.oss-ap-southeast-1.aliyuncs.com/forum/39ad14ec-7469-424e-b0c8-6d4a160299d2.png) and the [GRBL instructions for wiring limit switches](https://github.com/gnea/grbl/wiki/Wiring-Limit-Switches) assemble a circuit the same as the "connecting normally opened (NO) end switches to GRBL (improved noise filtering) ignoring the z-axis.  This will use up:
   * 2 x 100nF (0.1uF or 104) capacitors
   * 2 x 4k7ohm resistors
   * 2 x 2-way screw terminals
   * 1 x 2x7 0.1" header socket
   * A small 7x12 hole piece of veroboard
1. Mount the limit switches
1. Connect each limit switch to the relevant 2-way terminal made in step 3
1. Upgrade the firmware on the on-board Arduino Nano (programmed using the traditional bootloader option) to use [GRBL](https://github.com/gnea/grbl) v1.1h (we used a version with the [spindle control modifications for servo](https://github.com/DWiskow/grbl1-1g-Servo) but the servo feature is not used at present)
   1. Check out the `break-the-frame` branch of the [MCQN fork of GRBL](https://github.com/mcqn/grbl/tree/break-the-frame)
   1. Build it by running `make`
   1. Upload it to the Arduino: `avrdude -Cavrdude.conf -v -patmega328p -carduino -P/dev/ttyUSB0 -b57600 -D -Uflash:w:grbl.hex:i` (If you have the Arduino IDE installed that will include a suitable version of `avrdude` and `avrdude.conf`)
1. Set the GRBL settings to match these:
```
$0=10
$1=25
$2=0
$3=0
$4=0
$5=0
$6=0
$10=1
$11=0.010
$12=0.002
$13=0
$20=1
$21=0
$22=1
$23=0
$24=100.000
$25=600.000
$26=250
$27=5.000
$30=255
$31=0
$32=0
$100=80.000
$101=80.000
$102=80.000
$110=5000.000
$111=5000.000
$112=5000.000
$120=200.000
$121=200.000
$122=200.000
$130=380.000
$131=260.000
$132=200.000
```

