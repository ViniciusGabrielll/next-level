#!/usr/bin/env pybricks-micropython
import time
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
    #ev3.print(left_sensor.reflection(), right_sensor.reflection())
    correction = erro * KP

    left_speed = base_speed + correction
    right_speed = base_speed - correction
    right_motor.dc(left_speed)
    left_motor.dc(right_speed)
def curve_right():
    if left_sensor.reflection() >= 27 and right_sensor.reflection() <=6:
        print("curva direita")
        ev3.speaker.beep()
        while not left_sensor.reflection() <= 6:
            left_motor.dc(-80)
            right_motor.dc(30)
def curve_left():
    if right_sensor.reflection() >= 27 and left_sensor.reflection() <= 6:
        print("curva esquerda")
        ev3.speaker.beep()
        while not right_sensor.reflection() <= 6:
            left_motor.dc(65)
            right_motor.dc(-95)
def pass_gap():
    if right_sensor.reflection() and left_sensor.reflection() >= 35:
        print("GAP DETECTADO")
        while right_sensor.reflection() and left_sensor.reflection() >= 35:
            print("DENTRO DO GAP")
            left_motor.dc(-70)
            right_motor.dc(-70)

while True:
    lineFollower(3)
    curve_right()
    if curve_right() == True:
        time.sleep(0.25)
    curve_left()
    if curve_left() == True:
        time.sleep(0.25)
    print(left_sensor.reflection(), right_sensor.reflection())
