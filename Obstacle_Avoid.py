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

obstacle_sensor = UltrasonicSensor(Port.S4)
while True:
    robot.drive(200,0)
    while obstacle_sensor.distance() > 300:
        wait(10)
    robot.drive_time(-100,0,2000)
    robot.drive_time(0,60,2000)
