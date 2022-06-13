"""task2_tests"""

import unittest
from flower import Flower, Tulip, Rose, Chamomile, FlowerSet, Bucket


class TestFlower(unittest.TestCase):
    """Class to test flower classes and connected ones."""

    def setUp(self):
        """Tools for testing Flower class."""

        self.flower1 = Flower("yellow", 4, 15)
        self.tulip = Tulip(4, 18)
        self.rose = Rose(18, 34)
        self.chamomile = Chamomile(7, 16)
        self.set1 = FlowerSet()
        self.set1.add_flower(self.flower1)
        self.set1.add_flower(self.tulip)
        self.set2 = FlowerSet()
        self.set2.add_flower(self.rose)
        self.bucket = Bucket()
        self.bucket.add_set(self.set1)
        self.bucket.add_set(self.set2)

    def test_flowers_eq(self):
        """Testing flowers` attributes."""
        self.assertEqual(self.flower1.color, "yellow")
        self.assertEqual(self.tulip.color, "pink")
        self.assertEqual(len(self.set1.flower_set), 2)

    def test_flowers_in(self):
        """Testing flowers` occurance."""
        self.assertIn(self.flower1, self.set1.flower_set)
        self.assertIn(self.set1, self.bucket.bucket)

    def test_flowers_instance(self):
        """Testing flowers` isinstance."""
        self.assertIsInstance(self.rose, Rose)
        self.assertIsInstance(self.bucket.total_price(), int)

    def test_flowers_exc1(self):
        """Testing flowers` errors."""
        self.assertRaises(TypeError, lambda: Flower("yellow", "4", 15))

    def test_flowers_exc2(self):
        """Testing flowers` errors."""
        self.assertRaises(ValueError, lambda: Flower("yellow", 4, -15))

    def test_flowers_exc3(self):
        """Testing flowers` errors."""
        self.assertRaises(TypeError, lambda: Flower(["yellow"], 4, 15))

    def test_flowers_exc4(self):
        """Testing flowers` errors."""
        self.assertRaises(ValueError,
        lambda: self.set2.add_flower(self.chamomile))

if __name__ == "__main__":
    unittest.main()
