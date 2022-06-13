"""lab5 2var task2"""


class Rational:
    """A class to represent math operations with rational numbers.

    Attributes
    ------------
        nominator: int
            nominator
        denominator: int
            denominator

    """
    def __init__(self, nominator, denominator):
        """Inits Rational class with nominator, denominator."""
        self.nominator = nominator
        self.denominator = denominator
    
    def __str__(self):
        """Shows the rational number when printed."""
        return f"{self.nominator}/{self.denominator}"

    def __add__(self, other):
        """Overloads the operation of addition."""
        new_denominator = self.denominator
        new_nominator = self.nominator + other.nominator
        if self.denominator != other.denominator:
            new_denominator *= other.denominator
            new_nominator = self.nominator*other.denominator+\
                other.nominator*self.denominator
        return Rational(new_nominator, new_denominator)

    def __sub__(self, other):
        """Overloads the operation of substraction."""
        new_denominator = self.denominator
        new_nominator = self.nominator - other.nominator
        if self.denominator != other.denominator:
            new_denominator *= other.denominator
            new_nominator = self.nominator*other.denominator-\
                other.nominator*self.denominator
        return Rational(new_nominator, new_denominator)

    def __mul__(self, other):
        """Overloads the operation of multiplication."""
        new_denominator = self.denominator*other.denominator
        new_nominator = self.nominator*other.nominator
        return Rational(new_nominator, new_denominator)

    def __truediv__(self, other):
        """Overloads the operation of division."""
        new_denominator = self.denominator*other.nominator
        new_nominator = self.nominator*other.denominator
        return Rational(new_nominator, new_denominator)


def test_rational():
    """Test function."""
    print("Testing class Rational ...")
    # This is an implementation of a Rational numbers
    # that consist of 2 parts - nominator and denominator.
    # You can imagine this Ratinal numbers as fractions
    # like 3/4
    rational1 = Rational(1, 4)
    assert (type(rational1) == Rational)
    assert (isinstance(rational1, Rational))
    assert (str(rational1) == "1/4")

    # here you can add two numbers
    rational2 = Rational(2, 5)
    assert (str(rational1 + rational2) == "13/20")

    # here is a substraction
    assert (str(rational1 - rational2) == "-3/20")

    # multiplication
    assert (str(rational1 * rational2) == "2/20")

    # division
    assert (str(rational1 / rational2) == "5/8")

    assert (type(rational1 + rational2) == Rational)
    assert (type(rational1 - rational2) == Rational)
    assert (type(rational1 * rational2) == Rational)
    assert (type(rational1 / rational2) == Rational)

    print("Done!")


if __name__ == '__main__':
    test_rational()
