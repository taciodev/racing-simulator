import random
import time


def set_new_car_position(position):
    position += random.randint(1, 10)
    return position


def main():
    print("Hello from racing!")

    total_distance = 50
    car1 = 0
    car2 = 0

    while True:
        car1 = set_new_car_position(car1)
        car2 = set_new_car_position(car2)
        print(f"Car 1: {car1}, Car 2: {car2}")
        time.sleep(2)

        if car1 >= total_distance:
            print("Car 1 wins!")
            break
        elif car2 >= total_distance:
            print("Car 2 wins!")
            break


if __name__ == "__main__":
    main()
