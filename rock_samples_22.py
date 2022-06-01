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
robot.turn(-15)
robot.straight(300)
robot.reset()
found = False
search = obstacle_sensor.distance()
while found == False:
    ev3.screen.print(str(search))
    if search < 400:
        found = True
    robot.turn(-2)
    search = obstacle_sensor.distance()
    wait(100)
robot.turn(-15)
robot.stop()
ang = robot.angle()
robot.reset()

# drive(drive_speed, turn_rate)
robot.drive(50,0)
while obstacle_sensor.distance() > 100:
    ev3.screen.print(str(obstacle_sensor.distance()))
    wait(5)
robot.stop()
dist = robot.distance()
robot.straight(-dist)
robot.turn(-ang)
robot.straight(-300)
