import pygame
import time

axisNames = [ "   X", "   Y", "   Z", "Trim" ]
pygame.init()

pygame.joystick.init()
count = pygame.joystick.get_count()
print("Count: ", count)
if count < 1:
    exit

joystick = pygame.joystick.Joystick(0)
print("Name:     ", joystick.get_name())

joystick.init()

numAxes = joystick.get_numaxes()
print ("Axes:    ", numAxes)

numButtons = joystick.get_numbuttons()
print ("Buttons: ", numButtons)

joystick.init()
while True:
    pygame.event.get()
    for i in range(0, numAxes):
        print(axisNames[i], ": ", joystick.get_axis(i))
    time.sleep(1)
