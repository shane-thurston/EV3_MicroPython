#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
arm_motor = Motor(Port.C)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for 100mm.
robot.straight(100)
ev3.speaker.beep()

robot.straight(-100)
ev3.speaker.beep()

#run arm motor (speed mm/s, rotational angle)
arm_motor.run_angle(-100,120)
# Go backwards for 100mm
robot.straight(-100)
#run arm motor (speed mm/s, rotational angle,wait for maneuver)
arm_motor.run_angle(-100,120,Stop.HOLD,False)
robot.straight(-200)
