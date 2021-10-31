# Part 1

# Car Can "See" and "Navigate" around obstables
import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.ultrasonic import Ultrasonic
import time
import random
speed = 30
threshold = 10
turn_threshold = 20
# create an Ultrasonic object

ua = Ultrasonic(Pin('D8'), Pin('D9'))

# keep driving straight, if an obstacle is "seen"
# stop the vehicle, turn, and check for obstacle again
# if no obstacle, keep driving

def main():
    while True:
        distance = ua.get_distance()
        print(distance)

        if distance < threshold and distance > 0:
            fc.backward(speed)
            time.sleep(0.5
        if distance < turn_threshold and distance > 0:
            rand = random.randint(0,2)
            if rand == 0:
                fc.turn_left(speed)
            else:
                fc.turn_right(speed)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
