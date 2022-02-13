import Jetson.GPIO as GPIO
import time

class Motor():
    def __init__(self, FirstPin, SecondPin, nFirstPin, nSecondPin):
        self.FirstPin=FirstPin
        self.SecondPin=SecondPin
        self.nFirstPin=nFirstPin
        self.nSecondPin=nSecondPin
        print("hello ans , Im here")
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup([self.FirstPin, self.SecondPin, self.nFirstPin, self.nSecondPin], GPIO.OUT, initial=0)
    

    def setStep(self, w1, w2, w3, w4):
        GPIO.output(self.FirstPin, w1)
        
        GPIO.output(self.SecondPin, w2)
       
        GPIO.output(self.nFirstPin, w3)
        
        GPIO.output(self.nSecondPin, w4)
        
    
# delay = speed, steps = distance

    def forward(self, delay, steps):
        print("start forward")
        print(delay)
        print(steps)
        for i in range(0, steps):
            self.setStep(1, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 0, 1, 1)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(1, 0, 0, 1)
            time.sleep(delay)
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            print("i:",i)
            
            

    def backward(self, delay, steps):
        print("start backward")
        for i in range(0, steps):
            self.setStep(1, 0, 0, 0)
            time.sleep(delay)
            self.setStep(1, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 0, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 1)
            time.sleep(delay)
            self.setStep(0, 0, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 1, 0)
            time.sleep(delay)
            self.setStep(0, 1, 0, 0)
            time.sleep(delay)
            self.setStep(1, 1, 0, 0)
            time.sleep(delay)
            print("i:",i)
            
    
    