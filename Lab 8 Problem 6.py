import math

def getInput():
    angle = input('Please enter an angle in degrees: ')
    angle_degrees = float(angle)
    return angle_degrees

def convertDeg(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    return angle_radians

def printResult(angle_degrees, angle_radians):
    print('The angle', angle_degrees, 'degrees is equal to', angle_radians:.3f, 'radians.')
