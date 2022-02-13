from step_motor_control import Motor
import time

IN1=21 #FirstPin = A
IN2=22 #SecondPin = B
IN3=23 #nFirstPin = nA
IN4=24 #nnSecondPin = nB

#start below 600steps/second  -> 2ms minimum
#maxium below 1000steps/second


#A -> B -> nA -> nB

motorA=Motor(IN1,IN2,IN3,IN4)
motorA.setStep(0,0,0,0)
motorA.forward(0.003,1000)
