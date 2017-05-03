import time
import sys
import RPi.GPIO as GPIO
import Adafruit_PCA9685

def BUSInit():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.OUT)
    GPIO.output(11, 1)
    time.sleep(0.1)
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(50)
    return pwm


def Main():
    pwm = BUSInit()
    try:
        i = False
        with open('ServoConfig.txt', 'w') as conf:
            print("Servo Pin 0: Maximum angle configuration(arround 500)")
            while i == False:
                servo = input("Servo Pin 0 - Input angle: ")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Servo Pin 0: \r\n')
                    conf.write('\r\nMax. Position: ' + servoold)
                    conf.write('\r\nAngle: ' + servoangle  + '\r\n')
                    
                else:
                    pwm.set_pwm(0,0,int(servo))
                    servoold = servo
                    
            i = False
            print("Servo Pin 0: Middle angle configuration(arround 350)")
            while i == False:
                servo = input("Servo Pin 0 - Input angle: ")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Mid. Position: ' + servoold +'\r\n')
                    conf.write('Angle: ' + servoangle + '\r\n')
                else:
                    pwm.set_pwm(0,0,int(servo))
                    servoold = servo
                    
            i = False
            print("Servo Pin 0: Minimum angle configuration(arround 150)")
            while i == False:
                servo = input("Servo Pin 0 - Input angle: ")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Min. Position: ' + servoold +'\r\n')
                    conf.write('Angle: ' + servoangle + '\r\n')
                    
                else:
                    pwm.set_pwm(0,0,int(servo))
                    servoold = servo

            i = False
            print("Servo Pin 1: Maximum angle configuration(arround 500)")
            while i == False:
                servo = input("Servo Pin 1 - Input angle: ")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Servo Pin 1:\r\n')
                    conf.write('Max. Position: ' + servoold +'\r\n')
                    conf.write('Angle: ' + servoangle + '\r\n')
                else:
                    pwm.set_pwm(1,0,int(servo))
                    servoold = servo

            i = False
            print("Servo Pin 1: Middle angle configuration(arround 350)")
            while i == False:
                servo = input("Servo Pin 1 - Input angle: ")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Mid. Position: ' + servoold)
                    conf.write('Angle: ' + servoangle + '\r\n')
                else:
                    pwm.set_pwm(1,0,int(servo))
                    servoold = servo
                    
            i = False
            print("Servo Pin 1: Minimum angle configuration(arround 150)")
            while i == False:
                servo = input("Servo Pin 1 - Input angle:\r\n")
                if servo == "":
                    i = True
                    servoangle = input("Please give the resultating angle (degrees)")
                    conf.write('Min. Position: ' + servoold +'\r\n')
                    conf.write('Angle: ' + servoangle + '\r\n')
                else:
                    pwm.set_pwm(1,0,int(servo))
                    servoold = servo
        conf.close()
        print("Configuration complete!")
        GPIO.output(11,0)
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.output(11,0)
        GPIO.cleanup()
        conf.close()
        sys.exit()

if __name__ == '__main__':
    Main()
