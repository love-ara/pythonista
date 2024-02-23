import unittest

from src.bullet import Bullet
from src.gun import Gun


class TestGun(unittest.TestCase):

    def setUp(self):
        self.gun = Gun("yghjc", 6, "op")

    def test_that_magazine_is_empty(self):
        self.assertTrue(self.gun.magazine_is_empty())

    def test_that_bullet_can_be_added_to_magazine(self):
        self.assertTrue(self.gun.magazine_is_empty)
        bull = Bullet("op")
        self.gun.load_magazine(bull)
        self.assertFalse(self.gun.magazine_is_empty())

    def test_that_bullet_can_reduce_when_shoot_is_fired(self):
        self.assertTrue(self.gun.magazine_is_empty())
        bull = Bullet("op")
        self.gun.load_magazine(bull)
        self.gun.shoot()
        self.assertTrue(self.gun.magazine_is_empty())

    def test_load7Bullet_theNumberOfBulletInMagazineIs6(self):
        self.assertTrue(self.gun.magazine_is_empty())
        bull = Bullet("op")
        for i in range(6):
            self.gun.load_magazine(bull)
        self.assertEqual(6, self.gun.number_of_bullet())

        self.gun.load_magazine(bull)
        self.assertNotEqual(7, self.gun.number_of_bullet())
