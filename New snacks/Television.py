class Television:

    def __init__(self):
        self.isOn = False
        self.volume = 0
        self.channel = 1

    def turn_on(self):
        self.isOn = True

    def turn_off(self):
        self.isOn = False

    def increase_volume(self, volume):
        if self.isOn:
            self.volume += 1

    def reduce_volume(self, volume):
        if self.isOn and self.volume > 1:
            self.volume -= 1

    def set_channel(self, channel):
        self.channel = channel


    # def change_channel(self):

