import random, time, threading

TOTAL_DISTANCE = 50
barreira = threading.Barrier(2)


class Car(threading.Thread):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.position = 0
        self.finished = False

    def run(self):
        print(f"[{self.model}] pronto para largar.")
        barreira.wait()  # Espera todos os carros estarem prontos
        print(f"[{self.model}] começou a corrida!")

        while True:
            step = random.randint(1, 10)
            self.position += step
            print(f"[{self.model}] avançou {step} → posição: {self.position}")
            time.sleep(1)

            if self.position >= TOTAL_DISTANCE:
                self.finished = True
                break


def main():
    print("Hello from racing!")

    fusca = Car("Fusca")
    ferrari = Car("Ferrari")

    fusca.start()
    ferrari.start()

    while True:
        if fusca.finished:
            print("\n🚗 Fusca venceu a corrida!")
            break
        elif ferrari.position >= TOTAL_DISTANCE:
            print("\n🏎️ Ferrari venceu a corrida!")
            break
        time.sleep(0.5)


    fusca.join()
    ferrari.join()
    print("\n🏁 Corrida finalizada.")


if __name__ == "__main__":
    main()
