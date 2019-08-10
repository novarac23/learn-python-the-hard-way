from nose.tools import *
from ex47.game import Room

def test_room():
    gold = Room("GoldRoom", "This room has gold you can grab")

    assert_equal(gold.name, "GoldRoom")

def test_room_paths():
    center = Room("Center", "This is a center room")
    back = Room("Back", "This room is back")

    center.add_paths({'center': center, 'back': back})

    assert_equal(center.go('center'), center)
