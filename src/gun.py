from src.magazine import Magazine


class Gun:
    def __init__(self, gun_type, magazine_capacity, bullet_type):
        self.__gun_type = gun_type
        self.__magazine = Magazine(magazine_capacity)
        self.__bullet_type = bullet_type

    def magazine_is_empty(self):
        return self.__magazine.is_empty()

    def load_magazine(self, *bullets):
        for bullet in bullets:
            if self.__bullet_type == bullet.get_bullet_type():
                self.__magazine.load_bullet(bullets)

    def shoot(self):
        self.__magazine.unload_bullet()
        return "Fired"

    def number_of_bullet(self):
        return self.__magazine.number_of_bullets()
