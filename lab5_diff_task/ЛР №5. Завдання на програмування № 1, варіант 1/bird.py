"""lab5 task1"""


def get_local_methods(clss):
    """A helper function to get the list of names of class methods."""
    import types
    # This is a helper function for the test function below.
    # It returns a sorted list of the names of the methods
    # defined in a class. It's okay if you don't fully understand it!
    result = []
    for var in clss.__dict__:
        val = clss.__dict__[var]
        if (isinstance(val, types.FunctionType)):
            result.append(var)
    return sorted(result)

class Egg:
    """A class to represent an egg."""

class Bird:
    """A class to represent a bird and info about it.

    Attributes
    ------------
        name: str
            name of the bird
        eggs: None|set
            contains the Egg class objects (default to None)

    """
    def __init__(self, name, eggs=None):
        """Inits the Bird class with name, eggs."""
        self.name = name
        self.eggs = eggs or set()

    def __repr__(self):
        """Represents the information about the class object."""
        egg_str = 'egg' if len(self.eggs) == 1 else 'eggs'
        return f'{self.name} has {len(self.eggs)} {egg_str}'

    def lay_egg(self):
        """Lays the egg and adds it to the set with eggs."""
        self.eggs.add(Egg())

    def count_eggs(self):
        """Counts the number of eggs in the set."""
        return len(self.eggs)

    def fly(self):
        """Ability to fly."""
        return "I can fly!"

    def get_eggs(self):
        """Returns the list with eggs."""
        return list(self.eggs)

class Penguin(Bird):
    """A class to represent a penguin and info about it.

    Attributes
    ------------
        name: str
            name of the bird
        eggs: None|set
            contains the Egg class objects (default to None)

    """

    def swim(self):
        """Ability to swim."""
        return 'I can swim!'

    def fly(self):
        """Unability to fly."""
        return 'No flying for me.'

class MessengerBird(Bird):
    """A class to represent a messenger-bird and info about it.

    Attributes
    ------------
        name: str
            name of the bird
        eggs: None|set
            contains the Egg class objects (default to None)
        message: str
            a message for bird to deliver

    """
    def __init__(self, name, eggs=None, message=''):
        """Inits the class MessengerBird with name, eggs, message."""
        super().__init__(name, eggs)
        self.message = message

    def deliver_message(self):
        """Delivers the message."""
        return self.message


def test_bird_classes():
    print("Testing Bird classes...", end="")
    # A basic Bird has a species name, can fly, and can lay eggs
    bird1 = Bird("Parrot")
    assert (type(bird1) == Bird)
    assert (isinstance(bird1, Bird))
    assert (bird1.fly() == "I can fly!")
    assert (bird1.count_eggs() == 0)
    assert (str(bird1) == "Parrot has 0 eggs")

    # here changes
    assert (bird1.lay_egg() is None)
    eggs = bird1.get_eggs()
    egg = eggs.pop()
    assert (type(egg) == Egg)
    assert (isinstance(egg, Egg))
    #here changes ends

    assert (bird1.count_eggs() == 1)
    assert (str(bird1) == "Parrot has 1 egg")
    bird1.lay_egg()
    assert (bird1.count_eggs() == 2)
    assert (str(bird1) == "Parrot has 2 eggs")
    assert (get_local_methods(Bird) == ['__init__', '__repr__', 'count_eggs',
    'fly', 'get_eggs', 'lay_egg'])

    # A Penguin is a Bird that cannot fly, but can swim
    bird2 = Penguin("Emperor Penguin")
    assert (type(bird2) == Penguin)
    assert (isinstance(bird2, Penguin))
    assert (isinstance(bird2, Bird))
    assert (bird2.fly() == "No flying for me.")
    assert (bird2.swim() == "I can swim!")
    bird2.lay_egg()
    assert (bird2.count_eggs() == 1)
    assert (str(bird2) == "Emperor Penguin has 1 egg")
    assert (get_local_methods(Penguin) == ['fly', 'swim'])

    # # A MessengerBird is a Bird that can optionally carry a message
    bird3 = MessengerBird("War Pigeon", message="Top-Secret Message!")
    assert (type(bird3) == MessengerBird)
    assert (isinstance(bird3, MessengerBird))
    assert (isinstance(bird3, Bird))
    assert (not isinstance(bird3, Penguin))
    assert (bird3.deliver_message() == "Top-Secret Message!")
    assert (str(bird3) == "War Pigeon has 0 eggs")
    assert (bird3.fly() == "I can fly!")

    bird4 = MessengerBird("Homing Pigeon")
    assert (bird4.deliver_message() == "")
    bird4.lay_egg()
    assert (bird4.count_eggs() == 1)
    assert (get_local_methods(MessengerBird) == ['__init__', 'deliver_message'])
    print('Done!')

if __name__ == '__main__':
    test_bird_classes()
