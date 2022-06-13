"""task1.b"""

import unittest
from square_preceding import square_preceding


class TestSquarePreceding(unittest.TestCase):
    """Class to test square_preceding function."""

    def test_not_empty(self):
        """Testing not empty list."""
        result1 = square_preceding([1, 2, 3])
        self.assertEqual(result1, [0, 1, 4])
        self.assertNotEqual(result1, [0, 1, 1])

    def test_empty(self):
        """Testing empty list."""
        result2 = square_preceding([])
        self.assertEqual(result2, [])
        self.assertNotEqual(result2, [1, 2, 3])

if __name__ == "__main__":
    unittest.main()
