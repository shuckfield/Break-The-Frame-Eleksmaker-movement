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

