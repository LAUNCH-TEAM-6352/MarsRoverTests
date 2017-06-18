import RPi.GPIO as GPIO
import time

# Program to test simple motor control using the RB-Wav-77
# RPi Motor Driver Board from RobotShop.

# The following define indices for the two motors:
LEFT = 0
RIGHT = 1

# The following define the GPIO pins used to control the two motors.
# Note that we use the BCM pin numbering scheme.

# For each motor there are three pins:
#   The first and second pins set motor direction
#   The third pin controls the PWM signal
MOTOR_PINS = [ [20, 21, 26], [6, 13, 12] ]

# Motor direction is set via two pins for each motor:
# Pin1  Pin2  Direction
# ====  ====  =========
#    0     0  Stopped
#    0     1  Reverse
#    1     0  Forward
#    1     1  Stopped

# The PWN frequency:
FREQ = 500

# Tells the specified motor to move in forward direction:
def forward(motor):
    GPIO.output(MOTOR_PINS[motor][0], 1)
    GPIO.output(MOTOR_PINS[motor][1], 0)

# Tells the specified motor to move in reverse direction:
def reverse(motor):
    GPIO.output(MOTOR_PINS[motor][0], 0)
    GPIO.output(MOTOR_PINS[motor][1], 1)

# Tells the specified motor to stop:
def stop(motor):
    GPIO.output(MOTOR_PINS[motor][0], 0)
    GPIO.output(MOTOR_PINS[motor][1], 0)

# Tells the specified motor to turn a a specified speed between -100 and 100:
def speed(motor, speedVal):
    # Set appropriate direction:
    if speedVal < 0:
        reverse(motor)
    else:
        forward(motor)

    # Set speed:
    PWMS[motor].ChangeDutyCycle(abs(speedVal))

# Here is the main program:

# Configure GPIO pins:
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
for m in range(LEFT, RIGHT + 1):
    for p in range(0, 3):
        GPIO.setup(MOTOR_PINS[m][p], GPIO.OUT)

# The following creates an array of two PWM channels, one for each motor:
PWMS = [ GPIO.PWM(MOTOR_PINS[LEFT][2], FREQ), GPIO.PWM(MOTOR_PINS[RIGHT][2], FREQ) ]

# Make sure everything is stopped:
stop(LEFT)
stop(RIGHT)
PWMS[LEFT].start(0)
PWMS[RIGHT].start(0)

while True:
    speedVal = int(input("Enter speed between -100 and 100: "))

    # If out of range quit:
    if abs(speedVal) > 100:
        stop(LEFT)
        PWMS[LEFT].start(0)
        stop(RIGHT)
        PWMS[RIGHT].start(0)
        break

    speed(LEFT, speedVal)
    speed(RIGHT, speedVal)

