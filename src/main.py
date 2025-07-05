from models.circuit import Circuit
from models.car import Car
from models.race import Race

def main():
    circuit = Circuit(name="Interlagos", length=10, laps=5, weather="rain")

    car1 = Car("Fusca", "🐢", circuit)
    car2 = Car("Ferrari", "🏎️", circuit)

    race = Race(circuit, [car1, car2])
    race.start()


if __name__ == "__main__":
    main()
