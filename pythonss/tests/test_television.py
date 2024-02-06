import pytest
from Television import Television

@pytest.fixture
def television():
    return Television()

def test_turned_on(television):
    television.turn_on()
    assert television.isOn

def test_turned_off(television):
    television.turn_on()
    television.turn_off()
    assert not television.isOn

def test_that_television_volume_can_be_increased(television):
    television.turn_on()
    television.increase_volume(1)
    television.increase_volume(2)
    assert television.volume == 2

def test_that_television_volume_can_be_decreased(television):
    television.turn_on()
    television.increase_volume(1)
    television.increase_volume(2)
    television.reduce_volume(1)
    assert television.volume == 1