
class Magazine(object):
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__magazines = []

    def is_empty(self):
        return self.__magazines == []

    def load_bullet(self, bullet):
        if len(self.__magazines) < self.__capacity:
            self.__magazines.append(bullet)

    def unload_bullet(self):
        self.__magazines.pop()

    def number_of_bullets(self):
        return len(self.__magazines)

