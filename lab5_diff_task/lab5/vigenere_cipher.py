"""lab6 task5, vigenere cipher"""


def combine_character(plain, keyword):
    """Calculate right for ciphertext character from two unencoded ones."""
    plain = plain.upper()
    keyword = keyword.upper()
    plain_num = ord(plain) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (plain_num + keyword_num) % 26)

def separate_character(cypher, keyword):
    """Calculate right character from ciphertext and unencoded character."""
    cypher = cypher.upper()
    keyword = keyword.upper()
    cypher_num = ord(cypher) - ord('A')
    keyword_num = ord(keyword) - ord('A')
    return chr(ord('A') + (cypher_num - keyword_num) % 26)


class VigenereCipher:
    """A class to represent a method of encoding text
    by using vigenere cipher.

    Attributes:
        keyword: keyword
            a word to encode

    """

    def __init__(self, keyword):
        """Inits VigenereCipher with keyword."""
        self.keyword = keyword

    def extend_keyword(self, number):
        """Calculates how much the keyword has to be repeated,
        so it can be encoded correctly."""
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]

    def _code(self, text, combine_func):
        """Helpful function for encoding and decoding methods."""
        text = text.replace(" ", "").upper()
        combined = []
        keyword = self.extend_keyword(len(text))
        for i,k in zip(text, keyword):
            combined.append(combine_func(i,k))
        return "".join(combined)

    def encode(self, plaintext):
        """Encoding method."""
        return self._code(plaintext, combine_character)

    def decode(self, ciphertext):
        """Decoding method."""
        return self._code(ciphertext, separate_character)
