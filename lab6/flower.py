"""task2"""


class Flower:
    """A class to represent flower and info about it.

    Attributes:
        color: str
            color of flower
        petals: int
            amount of petals
        price: int
            price of flower

    """

    def __init__(self, color, petals, price):
        """Inits Flower with color, petals, price."""
        self.color = self.color_checker(color)
        self.petals = self.numbers_checker(petals, to_insert="Amount of petals")
        self.price = self.numbers_checker(price, to_insert="Price")

    @staticmethod
    def color_checker(value):
        """Checks if color is string."""
        if not isinstance(value, str):
            raise TypeError("color should be a string!")
        else:
            return value

    @staticmethod
    def numbers_checker(value, to_insert=""):
        """Checks if petals and price are integers."""
        if not isinstance(value, int):
            raise TypeError(f"{to_insert} should be integer!")
        elif value < 0:
            raise ValueError(f"{to_insert} shouldn`t be negative!")
        else:
            return value

class Tulip(Flower):
    """A class to represent tulip and info about it.

    Attributes:
        color: str
            color of flower == pink
        petals: int
            amount of petals
        price: int
            price of flower

    """

    def __init__(self, petals, price):
        """Inints Tulip with petals and price, color is by default."""
        super().__init__("pink", petals, price)

class Rose(Flower):
    """A class to represent rose and info about it.

    Attributes:
        color: str
            color of flower == rose
        petals: int
            amount of petals
        price: int
            price of flower

    """

    def __init__(self, petals, price):
        """Inints Rose with petals and price, color is by default."""
        super().__init__("red", petals, price)

class Chamomile(Flower):
    """A class to represent chamomile and info about it.

    Attributes:
        color: str
            color of flower == white
        petals: int
            amount of petals
        price: int
            price of flower

    """

    def __init__(self, petals, price):
        """Inints Chamomile with petals and price, color is by default."""
        super().__init__("white", petals, price)


class FlowerSet:
    """A class to represent flowerset with flowers of the same class.

    Attributes:
        flower_set: set
            set with flowers as objects of flowery classes
        price: 0|int
            price of the flowerset

    """

    def __init__(self):
        """Inits Flowerset."""
        self.flower_set = set()
        self.price = 0

    def add_flower(self, flower):
        """Adds flowers to the flower_set and counts its price."""
        for elem in self.flower_set:
            if not isinstance(flower, type(elem)):
                raise ValueError("Only flowers of the same type can be in one set.")
        self.flower_set.add(flower)
        self.price += flower.price

class Bucket:
    """A class to represent a bucket with flowersets.

    Attributes:
        bucket: set
            set with flowersets as objects of FlowerSet
        price: 0|int
            price of the bucket

    """

    def __init__(self):
        """Inits Bucket."""
        self.bucket = set()
        self.price = 0

    def add_set(self, flower_set):
        """Adds flowersets to the bucket and counts its price."""
        self.bucket.add(flower_set)
        self.price += flower_set.price

    def total_price(self):
        """Returns the total price of the bucket."""
        return self.price
