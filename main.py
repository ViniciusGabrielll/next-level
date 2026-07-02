#!/usr/bin/env pybricks-micropython
import time
from pybricks.hubs import EV3Brick
from pybricks.parameters import Color
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase
from pybricks.tools import wait
from pybricks.ev3devices import UltrasonicSensor

ev3 = EV3Brick()
ev3.speaker.beep()

#sensor de giro
gyro = GyroSensor(Port.S4)
gyro.reset_angle(0)

#sensor ultrassonico
ultrasonic_sensor = UltrasonicSensor(Port.S1)

#motores e sensores
left_motor = Motor(Port.C)
right_motor = Motor(Port.B)
left_sensor = ColorSensor(Port.S3)
right_sensor = ColorSensor(Port.S2)

base_speed = -40
diametro_roda = 56
distancia_eixos = 114
robot = DriveBase(left_motor, right_motor, wheel_diameter=diametro_roda, axle_track=distancia_eixos)

def lineFollower(KP, velocidade):
    erro = left_sensor.reflection() - right_sensor.reflection()
    correction = erro * KP
    left_speed = velocidade - correction
    right_speed = velocidade + correction
    #print("correção: ", correction)
    right_motor.dc(-left_speed)
    left_motor.dc(-right_speed)

def girar_graus(graus):
    gyro.reset_angle(0)
    if graus > 0:
        left_motor.dc(-70)
        right_motor.dc(70)
        while gyro.angle() < 40:
            print("Giro: ", gyro.angle())
            wait(10) 

    elif graus < 0: 
        left_motor.dc(70)
        right_motor.dc(-70)
        while gyro.angle() > -40:
            print("Giro: ", gyro.angle())
            wait(10)

def girar_graus2(graus):
    gyro.reset_angle(0)
    if graus > 0: 
        left_motor.dc(-70)
        right_motor.dc(70)
        while gyro.angle() < 60:
            print("Giro: ", gyro.angle())
            wait(10)

    elif graus < 0:
        left_motor.dc(70)
        right_motor.dc(-70)
        while gyro.angle() > -60:
            print("Giro: ", gyro.angle())
            wait(10)

def girar_graus3(graus):
    if graus == 67: #six seven aura maxima
        left_motor.dc(-70)
        right_motor.dc(70)
        while gyro.angle() < 45: 
            print("Giro: ", gyro.angle())
            wait(10)  

def pararMotores():
    left_motor.stop()
    right_motor.stop()

fazendo_curva = False
while True:
    distancia = ultrasonic_sensor.distance()
    #passar das curvas
    left_reflection = left_sensor.reflection()
    right_reflection = right_sensor.reflection()
    if right_reflection >= 20 and right_reflection <= 100 and left_reflection >= 3 and left_reflection <= 26 or right_reflection >= 3 and right_reflection <= 19 and left_reflection >= 20 and left_reflection <= 100:
        print("Curva detectada \n")
        lineFollower(5, 40)
        fazendo_curva = True
    else:
        lineFollower(3.5, 44)
        fazendo_curva = False
        
    #passar dos verdes
    """if fazendo_curva == False:
        if left_reflection <= 4 or right_reflection <= 4:
            wait(100)
            left_color = left_sensor.color()
            right_color = right_sensor.color()
            if left_reflection >= 6 or right_reflection >= 6:
                pass
            if left_color != Color.GREEN or right_color != Color.GREEN:
                left_reflection = left_sensor.reflection()
                right_reflection = right_sensor.reflection()
            if left_color == Color.GREEN and right_color == Color.GREEN:
                left_reflection = left_sensor.reflection()
                right_reflection = right_sensor.reflection()
                print("Duplo Verde - Meia Volta")
                left_motor.dc(-60)
                right_motor.dc(-60)
                wait(300)
                left_motor.dc(-70)
                right_motor.dc(90)
                while gyro.angle() < 115: 
                    print("Giro: ", gyro.angle())
                    wait(10)
                    if left_sensor.reflection() <= 15 and right_sensor.reflection() <= 15:
                        continue
            elif left_color == Color.GREEN and right_color != Color.GREEN:
                left_reflection = left_sensor.reflection()
                right_reflection = right_sensor.reflection()
                print("Verde na Esquerda")
                left_motor.dc(-60)
                right_motor.dc(-60)
                wait(400)
                girar_graus(-90)
            elif right_color == Color.GREEN and left_color != Color.GREEN:
                left_reflection = left_sensor.reflection()
                right_reflection = right_sensor.reflection()
                print("Verde na Direita")
                left_motor.dc(-60)
                right_motor.dc(-60)
                wait(400)
                girar_graus(90)
            if left_color != Color.GREEN or right_color != Color.GREEN:
                left_sensor.reflection()
                right_sensor.reflection()"""
    
    #passar dos obstáculos
    if distancia <= 100:
        print("Objeto detectado a ", distancia, "cm")
        left_motor.dc(60)
        right_motor.dc(60)
        wait(80)
        gyro.reset_angle(0)
        girar_graus2(-90)
        pararMotores()
        left_motor.dc(-60)
        right_motor.dc(-60)
        wait(1500)
        gyro.reset_angle(0)
        girar_graus2(110)
        pararMotores()
        left_motor.dc(-60)
        right_motor.dc(-60)
        wait(2300)
        gyro.reset_angle(0)
        girar_graus3(67)
    print("Cor Esquerdo: ", left_sensor.reflection(), "Cor Direita: ", right_sensor.reflection())
    #print(gyro.angle())
    #print("Distância: ", distancia)
    wait(15)
