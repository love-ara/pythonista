import unittest
from src.sevensegment import SevenSegment


class TestSevenSegmentDisplay(unittest.TestCase):
    def setUp(self):
        self.segment = SevenSegment()

    def test_display_00000000(self):
        self.segment.display_segment("00000000")
        self.assertEqual(self.segment.digit, [["  "] * 4 for _ in range(5)])

    def test_display_11110011(self):
        self.segment.display_segment("11110011")
