# Part 1

# Car Can "See" and "Navigate" around obstables
import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.pwm import PWM
from picar_4wd.ultrasonic import Ultrasonic
from picar_4wd.servo import Servo
import time
speed = 25
threshold = 20
# create an Ultrasonic object

ua = Ultrasonic(Pin('D8'), Pin('D9'))
servo = Servo(PWM("P0"), offset=0)

# from init.py
def get_distance_at(angle):
    global angle_distance
    servo.set_angle(angle)
    distance = ua.get_distance()
    angle_distance = [angle, distance]
    return distance

# keep driving straight, if an obstacle is "seen"
# stop the vehicle, turn, and check for obstacle again
# if no obstacle, keep driving

def main():
    while True:
        distance = get_distance_at(0)
        print(distance)

        if distance < 0:
            continue
        elif distance < 5:
            fc.backward(speed)
        elif distance < threshold:
            fc.turn_right(speed)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
