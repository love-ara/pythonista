class AutomaticBike:
    def __init__(self):
        self.isOn = False
        self.speed = 0
        self.gear = 1

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def accelerate(self):
        if self.isOn:
            self.speed += self.gear
            self.update_gear()

    def decelerate(self):
        if self.isOn and self.speed > 0:
            self.speed -= self.gear
            self.update_gear()

    def update_gear(self):
        if self.speed <= 20:
            self.gear = 1
        elif 21 <= self.speed <= 30:
            self.gear = 2
        elif 31 <= self.speed <= 40:
            self.gear = 3
        else:
            self.gear = 4
