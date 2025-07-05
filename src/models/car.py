import threading
import random
import time

CRITICAL_SECTION = (20, 30)
critical_section_lock = threading.Lock()
barrier = threading.Barrier(2)
finish_order = []


class Car(threading.Thread):
    def __init__(self, name, icon, circuit):
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

            next_position = self.position + step

            if CRITICAL_SECTION[0] <= next_position <= CRITICAL_SECTION[1]:
                with critical_section_lock:
                    print(f"{self.name} 🚧 entrou na zona crítica!")
                    time.sleep(0.3)
                    self.position = next_position
                    print(f"{self.name} 🚧 saiu da zona crítica!")
            else:
                self.position = min(next_position, self.circuit.total_distance)

            time.sleep(0.3)

        self.finished = True
        finish_order.append(self.name)
