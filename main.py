#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait

# Inicializa o tijolo EV3 e emite um som de início
ev3 = EV3Brick()
ev3.speaker.beep()

# Configura os motores nas portas B e C
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)
left_sensor = ColorSensor(Port.S3)
right_sensor = ColorSensor(Port.S2)

base_speed = -40

# Cria a base de condução (DriveBase)
# Defina o diâmetro da roda (em mm) e a distância entre elas (em mm)
# Substitua os valores pelos tamanhos reais do seu robô
diametro_roda = 56
distancia_eixos = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter=diametro_roda, axle_track=distancia_eixos)

def lineFollower(KP):
    erro = left_sensor.reflection() - right_sensor.reflection()
    correction = erro * KP


    left_speed = base_speed - correction
    right_speed = base_speed + correction
    right_motor.dc(left_speed)
    left_motor.dc(right_speed)
def curve_right():
    if left_sensor.color() == Color.WHITE and right_sensor.color() == Color.BLACK:
        ev3.speaker.beep()
        while not left_sensor.color() == Color.BLACK:
            left_motor.dc(70)
            right_motor.dc(-70)
while True:
    lineFollower(1.2)
    curve_right()
