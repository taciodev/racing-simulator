import os
import time
from models.car import Car, finish_order


class Race:
    def __init__(self, circuit, cars: list[Car]):
        self.circuit = circuit
        self.cars = cars
        self.total_distance = circuit.total_distance
        self.start_time = None

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_race(self):
        self.clear_screen()
        print(f"🏁 Corrida em andamento no circuito {self.circuit.name}\n")
        print(f"🔒 Zona crítica: posições {20} até {30}\n")

        for car in self.cars:
            track = "-" * car.position + car.icon + "-" * (self.total_distance - car.position)
            print(f"{car.name.ljust(10)} | {track[:self.total_distance + 1]}")
        print()

    def start(self):
        print(f"\n🏟️ Circuito: {self.circuit.name} | Clima: {self.circuit.weather}")
        print(f"📏 Distância total: {self.total_distance} unidades\n")
        print("Aguardando todos os carros...")

        for car in self.cars:
            car.start()

        self.start_time = time.time()

        while not all(car.finished for car in self.cars):
            self.draw_race()
            time.sleep(0.1)

        self.end_race()

    def end_race(self):
        assert self.start_time is not None, "start_time não pode ser None"
        elapsed_time = round(time.time() - self.start_time, 2)
        print("🏁 Corrida finalizada!\n")
        print("📊 Resultado:")
        for i, name in enumerate(finish_order, start=1):
            print(f"{i}º lugar: {name}")
        print(f"\n⏱️ Tempo total: {elapsed_time} segundos")
