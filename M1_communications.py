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

robot.drive_time(100, 0, 3600) #Drive forward 36cm
robot.drive_time(0, -55, 1000) #Turn left
robot.drive_time(100, 0, 2500) #Drive forward 25cm
robot.stop()

#You need to perform the same actions in reverse to complete challenge
