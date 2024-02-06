import pytest
from Automatic_bike import AutomaticBike


@pytest.fixture
def bike():
    return AutomaticBike()


def test_turn_on(bike):
    bike.turn_on()
    assert bike.isOn


def test_turn_off(bike):
    bike.turn_on()
    bike.turn_off()
    assert not bike.isOn


def test_accelerate(bike):
    bike.turn_on()
    bike.accelerate()
    assert bike.speed == 1


def test_decelerate(bike):
    bike.turn_on()
    bike.accelerate()
    bike.decelerate()
    assert bike.speed == 0


@pytest.mark.parametrize("accel_steps, expected_speed", [(25, 2), (10, 1)])
def test_gear_change(bike, accel_steps, expected_speed):
    bike.turn_on()

    for _ in range(accel_steps):
        bike.accelerate()

    assert bike.gear == expected_speed
