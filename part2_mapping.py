import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.pwm import PWM
from picar_4wd.ultrasonic import Ultrasonic
from picar_4wd.servo import Servo
import numpy as np
import time
import sys

ua = Ultrasonic(Pin('D8'), Pin('D9'))
servo = Servo(PWM("P0"), offset=0)
# from init.py
def get_distance_at(angle):
    global angle_distance
    servo.set_angle(angle)
    time.sleep(0.04)
    distance = us.get_distance()
    angle_distance = [angle, distance]
    return distance

def generate_map():
    angles = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]
    # Scan the surroundings
    # store results as array of [angle, distance]
    raw_data = []
    for angle in angles:
        distance = ua.get_distance_at(angle)
        if distance < 0:
            distance = 999
        raw_data.append([angle, distance])
    print(raw_data)
    # Process array
    # [0/1 , y, x]
    #  50*sqrt(2) approx 71
    # points = []
    # for d in distances:
    #
    #
    # # Fill out numpy array
    # map = np.zeros((50,100))
    #
    # np.set_printoptions(threshold=sys.maxsize)
    # print(arr)

if __name__ == '__main__':
    generate_map()
