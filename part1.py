# Part 1

# Car Can "See" and "Navigate" around obstables
import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.ultrasonic import Ultrasonic
import time
speed = 25
# create an Ultrasonic object
ua = Ultrasonic(Pin('D8'), Pin('D9'))

# keep driving straight, if an obstacle is "seen"
# stop the vehicle, turn, and check for obstacle again
# if no obstacle, keep driving

def main():
    while True:
        distance = ua.get_distance()
        print(distance)

        if distance < 10:
            fc.backward(speed)
            time.sleep(0.04)
        if distance < 40:
            fc.turn_right(speed)
            time.sleep(0.04)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
