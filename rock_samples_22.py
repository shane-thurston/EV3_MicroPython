#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Create your objects here.
ev3 = EV3Brick()
# Write your program here
left = Motor(Port.A)
right = Motor(Port.B)
robot = DriveBase(left,right,56,114)

obstacle_sensor = UltrasonicSensor(Port.S4)
robot.straight(300)
robot.reset()
while obstacle_sensor.distance() > 500:
    robot.turn(-2)
    wait(15)
robot.stop()
ang = robot.angle()
robot.reset()
# drive(drive_speed, turn_rate)
robot.drive(100,0)
while obstacle_sensor.distance() > 100:
    wait(5)
robot.stop()
dist = robot.distance()
robot.straight(-dist)
robot.turn(-ang)
robot.straight(-300)
