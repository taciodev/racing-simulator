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
