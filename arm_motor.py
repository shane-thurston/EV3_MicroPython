#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Setup drive base
left = Motor(Port.A)
right = Motor(Port.B)
robot = DriveBase(left,right,56,114)

# Setup arm motor
arm_motor = Motor(Port.C)

#drive_time(speed:mm/s, steering:deg/s, time:ms)
robot.drive_time(100, 0, 1000) #Drive forward 10cm

robot.stop()

#run arm motor (speed mm/s, rotational angle)
arm_motor.run_angle(100,60)
