# Part 1

# Car Can "See" and "Navigate" around obstables
import picar_4wd as fc
from picar_4wd.pin import Pin
from picar_4wd.ultrasonic import Ultrasonic
import time
speed = 25
too_close = 30
threshold = 50
# create an Ultrasonic object
ua = Ultrasonic(Pin('D8'), Pin('D9'))

def avoid_obstacle():
    distance = ua.get_distance()
    # back away from obstacle if too close
    while(distance < too_close):
        time.sleep(0.04)
        fc.backward(speed)
        distance = ua.get_distance()

    while(1):
        # default is try to go right around the obstacle
        fc.turn_right(speed)
        distance = ua.get_distance()
        if distance >= threshold:
            fc.forward(speed)
            fc.turn_left(speed)
            left_dist = ua.get_distance()
            if left_dist > distance:
                break
            fc.turn_right(speed)
        distance = ua.get_distance()
        if distance >= threshold:
            break

# keep driving straight, if an obstacle is "seen"
# stop the vehicle, turn, and check for obstacle again
# if no obstacle, keep driving

def main():
    while True:
        distance = ua.get_distance()
        print(distance)

        if distance < 0:
            continue
        elif distance < threshold:
            avoid_obstacle()
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
