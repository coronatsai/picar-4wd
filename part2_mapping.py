import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.pwm import PWM
from picar_4wd.ultrasonic import Ultrasonic
from picar_4wd.servo import Servo
import numpy as np
import time
import sys
import math

ua = Ultrasonic(Pin('D8'), Pin('D9'))
servo = Servo(PWM("P0"), offset=0)
# from init.py
def get_distance_at(angle):
    global angle_distance
    servo.set_angle(angle)
    time.sleep(1)
    distance = ua.get_distance()
    angle_distance = [angle, distance]
    return distance

def generate_map():
    angles = [-90, -75, -60, -45, -30, -15, 0, 15, 30, 45, 60, 75, 90]
    # Scan the surroundings
    # store results as array of [angle, distance]
    raw_data = []
    for angle in angles:
        distance = get_distance_at(angle)
        if distance < 0:
            distance = 999
        raw_data.append([angle, distance])
    print(raw_data)
    # Process array
    # [0/1 , x, y]
    points = []
    for rd in raw_data:
        x = math.floor(rd[1] * math.cos(math.radians(rd[0])))
        y = math.floor(rd[1] * math.sin(math.radians(rd[0])))
        if x >= 30 or y >= 30:
            points.append([0, x, y])
        else:
            points.append([1, x, y])
    print(points)
    # # Fill out numpy array
    map = np.zeros((30,60))

    x_center = 30
    prev_point_val = 0
    prev_x = 0
    prev_y = 0
    for point in points:
        val = point[0]
        x = point[1]
        y = point[2]

        if val == 1:
            # Fill this point
            map[y , x_center + x] = 1
            if prev_point_val == 1:
                # draw a rectangle around the two points
                for i in range(prev_x, x):
                    for j in range(prev_y, y):
                        map[j, x_center + i] = 1
        prev_point_val = val
        prev_x = x
        prev_y = y
    np.asarray(map)
    print(map)

if __name__ == '__main__':
    generate_map()
