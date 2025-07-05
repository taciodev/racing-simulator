import random, time, threading, os

barrier = threading.Barrier(2)
finish_order = []
start_time = None


class Circuit:
    def __init__(self, name, length, laps, weather):
        self.name = name
        self.length = length
        self.laps = laps
        self._weather = None
        self.weather = weather

    @property
    def weather(self):
        return self._weather

    @weather.setter
    def weather(self, value):
        if value not in ("rain", "sunny"):
            raise ValueError("Weather must be 'rain' or 'sunny'")
        self._weather = value

    @property
    def total_distance(self):
        return self.length * self.laps


class Car(threading.Thread):
    def __init__(self, name, icon, circuit: Circuit):
        super().__init__()
        self.name = name
        self.icon = icon
        self.position = 0
        self.finished = False
        self.circuit = circuit

    def run(self):
        global finish_order
        barrier.wait()
        while self.position < self.circuit.total_distance:
            step = random.randint(1, 10)
            if self.circuit.weather == "rain":
                step = int(step * 0.7)

            self.position += step
            self.position = min(self.position, self.circuit.total_distance)
            time.sleep(0.3)

        self.finished = True
        finish_order.append(self.name)


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_race(cars, total_distance):
    clear_screen()
    print(f"🏁 Race in progress at {cars[0].circuit.name} Circuit\n")
    for car in cars:
        track = "-" * car.position + car.icon + "-" * (total_distance - car.position)
        print(f"{car.name.ljust(10)} | {track[:total_distance+1]}")
    print()


def main():
    global start_time

    circuit = Circuit(name="Interlagos", length=10, laps=5, weather="rain")
    total_distance = circuit.total_distance

    print(f"\n🏟️ Circuit: {circuit.name} | Weather: {circuit.weather}")
    print(f"📏 Total Distance: {total_distance} units\n")
    print("Waiting for all cars...")

    car1 = Car("Beetle", "🐢", circuit)
    car2 = Car("Ferrari", "🏎️", circuit)

    cars = [car1, car2]

    car1.start()
    car2.start()

    start_time = time.time()

    while True:
        draw_race(cars, total_distance)
        if all(car.finished for car in cars):
            break
        time.sleep(0.1)

    elapsed_time = round(time.time() - start_time, 2)

    print("🏁 Race finished!\n")
    print("📊 Results:")
    for i, name in enumerate(finish_order, start=1):
        print(f"{i}st place: {name}")

    print(f"\n⏱️ Elapsed Time: {elapsed_time} seconds")


if __name__ == "__main__":
    main()
