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

#Write the settings into file
#Called after AngleConfiguration found best settings
def Writer(pin,position,var):
    try:
        with open(file, 'w+') as conf: 
            conf.write("[PIN %s]: %s position: %s\r\n"%(pin,position,var[0]))
            conf.write("[PIN %s]: Angle: %s\r\n"%(pin,var[1]))
            conf.close() #not sure if necessary
    except IOError as ie:
        print ("Open file not possible: %s"%ie)

#Adjust the configuration of puls modulation
#Idea:      iterate through most likely positions automatically
#           and user have only to press a "stop" button when in
#           correct position, afterwards fine tuning
def AngleConfiguration(pin, position):
    Bool = False
    servoold = None
    while Bool == False:
        servo = input("[PIN %s]:Input angle: "%pin)
        
        if servo == "" and servoold is not None:
            Bool = True
            #GPIO.cleanup()
            servoangle = input("Please give the resultating angle (degrees)")            
            Writer(pin,position,(servoold,servoangle))            
        else:
            if servo != "":
                if int(servo) > LOWER_BOUND and int(servo) < UPPER_BOUND:
                    pwm.set_pwm(pin,0,int(servo))
                    servoold = servo
                else:
                    print("The min value is %d and the max value is %d"%(LOWER_BOUND,UPPER_BOUND))
            else:
                print("At least one entry is necessary!")

#Connect to servomotor of connected pins from pi to and.
#Idea:  Dynamic by parameter 
def PinConfiguration():
    try:
        with open(file, 'a+') as conf: #filehandle creates file now if not existing
            conf.close()
            try:       
                #PIN0
                outputpin = 0
                #CallBoundarySetting
                print("[PIN %s]: Maximum angle configuration(around 500)"%outputpin)
                AngleConfiguration(outputpin,"max")
                print("[PIN %s]: Middle angle configuration(around 350)"%outputpin)
                AngleConfiguration(outputpin,"middle")                          
                print("[PIN %s]: Minimum angle configuration(around 150)"%outputpin)
                AngleConfiguration(outputpin,"min")
                #PIN1
                outputpin = 1
                print("[PIN %s]: Maximum angle configuration(around 500)"%outputpin)
                AngleConfiguration(outputpin,"max")
                print("[PIN %s]: Middle angle configuration(around 350)"%outputpin)
                AngleConfiguration(outputpin,"middle")                          
                print("[PIN %s]: Minimum angle configuration(around 150)"%outputpin)
                AngleConfiguration(outputpin,"min")                       
                print("Configuration complete!")
                GPIO.output(11,0)
                GPIO.cleanup()                
            except KeyboardInterrupt as ki:
                print ("Error occured read keyboard input: %s "%ki)
                GPIO.output(11,0)
                GPIO.cleanup()
                conf.close()
                sys.exit()
    except IOError:
        print("Open file not possible")

if __name__ == '__main__':  
    #define bushandle for all            
    pwm = BUSInit()  
    #name of file or parameter input
    file = 'ServoConfig.txt'
    #define constants to avoid crashing the servomotors
    UPPER_BOUND = 400
    LOWER_BOUND = 180
    
    PinConfiguration()
