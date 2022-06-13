"""tests for lab6 task5, vigenere cipher"""

from unittest import TestCase, main
from vigenere_cipher import VigenereCipher, separate_character, combine_character


def test_encode():
    """Test encode method."""
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODEDINPYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_character():
    """Test encoding with characters."""
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("E")
    assert encoded == "X"

def test_encode_spaces():
    """Test encodeing with spaces."""
    cipher = VigenereCipher("TRAIN")
    encoded = cipher.encode("ENCODED IN PYTHON")
    assert encoded == "XECWQXUIVCRKHWA"

def test_encode_lowercase():
    """Test encoding with lowercase."""
    cipher = VigenereCipher("TRain")
    encoded = cipher.encode("encoded in Python")
    assert encoded == "XECWQXUIVCRKHWA"

def test_extend_keyword():
    """Test extend_keyword method."""
    cipher = VigenereCipher("TRAIN")
    extended = cipher.extend_keyword(16)
    assert extended == "TRAINTRAINTRAINT"

def test_separate_character():
    """Test the separate_character function.."""
    assert separate_character("X", "T") == "E"
    assert separate_character("E", "R") == "N"

def test_combine_character():
    """Test the combine_character function."""
    assert combine_character("E", "T") == "X"
    assert combine_character("N", "R") == "E"

def test_decode():
    """Test decode method."""
    cipher = VigenereCipher("TRAIN")
    decoded = cipher.decode("XECWQXUIVCRKHWA")
    assert decoded == "ENCODEDINPYTHON"

def pytest_tests():
    """Runs all tests."""
    test_encode()
    test_encode_character()
    test_encode_spaces()
    test_encode_lowercase()
    test_extend_keyword()
    test_separate_character()
    test_combine_character()
    test_decode()
    print("PyTests passed!")


class TestVigenereCipher(TestCase):
    """Class for testing vigenere_cipher module with unittest."""

    def setUp(self):
        """Sets cipher for using while testing."""
        self.cipher = VigenereCipher("TRAIN")

    def test_encode_uni(self):
        """Test encode method."""
        self.assertEqual(self.cipher.encode("ENCODEDINPYTHON"), "XECWQXUIVCRKHWA")

    def test_encode_character_uni(self):
        """Test encoding with characters."""
        self.assertEqual(self.cipher.encode("E"), "X")

    def test_encode_spaces_uni(self):
        """Test encodeing with spaces."""
        self.assertIsNot(self.cipher.encode("ENCODED IN PYTHON"), "XECWQXUIVCRKHWH")

    def test_encode_lowercase_uni(self):
        """Test encoding with lowercase."""
        self.assertEqual(self.cipher.encode("encoded in Python"), "XECWQXUIVCRKHWA")

    def test_extend_keyword_uni(self):
        """Test extend_keyword method."""
        self.assertEqual(self.cipher.extend_keyword(16), "TRAINTRAINTRAINT")

    def test_separate_character_uni(self):
        """Test the separate_character function.."""
        self.assertEqual(separate_character("X", "T"), "E")

    def test_combine_character_uni(self):
        """Test the combine_character function."""
        self.assertEqual(combine_character("N", "R"), "E")

    def test_decode_uni(self):
        """Test decode method."""
        self.assertEqual(self.cipher.decode("XECWQXUIVCRKHWA"),"ENCODEDINPYTHON")
        print("UnitTests passed!")

if __name__ == "__main__":
    pytest_tests()
    main()
