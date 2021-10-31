# Part 1

# Car Can "See" and "Navigate" around obstables
import picar_4wd as fc
from picar_4wd.Ultrasonic import Ultrasonic

speed = 20
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
            fc.turn_right(speed)
        elif distance < 30:
            fc.turn_right(speed)
        else:
            fc.forward(speed)

if __name__ == "__main__":
    try:
        main()
    finally:
        fc.stop()
