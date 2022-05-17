#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase

# Create your objects here.
ev3 = EV3Brick()

# Initialize the Ultrasonic Sensors.
obstacle_sensor = UltrasonicSensor(Port.S1)
color_sensor = ColorSensor(Port.S4)

# Initialize two motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
arm_motor = Motor(Port.D)

# The DriveBase is composed of two motors, with a wheel on each motor.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#drive_time(speed:mm/s, steering:deg/s, time:ms)
robot.drive_time(100, 0, 1000) #Drive forward 10cm
robot.stop()

#run arm motor (speed mm/s, rotational angle)
arm_motor.run_angle(-100,60)

#run time with wait as FALSE
#run_time(speed deg/s, time ms, then=Stop.HOLD, wait=True)
left_motor.run_time(-100,1000,Stop.HOLD,False)
right_motor.run_time(-100,1000,Stop.HOLD,False)
arm_motor.run_time(50,1000,Stop.HOLD,False)
wait(1000)
