#!/usr/bin/env pybricks-micropython
from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left,right,56,114)

#drive_time(speed:mm/s, steering:deg/s, time:ms)
#(90 degrees)
robot.drive_time(0, 90, 1000)
robot.stop()
