'''module with classes for main'''


class Room:
    '''A class to represent the room and info about it.

    Attributes:
        name: str
            name of the room
        description: str
            description of the room
        neighbour: Room
            the following room
        wrld_side: str
            one of 4 sides of the world
        character: Character
            character in the room
        item: Item
            item in the room
        linkings: list
            list with str about neighbours and sides
        info: dict
            dict with neighbours as values and sides as keys

    '''

    description = ''
    neighbour = None
    wrld_side = ''
    character = None
    item = None

    def __init__(self, name):
        '''Inits Room with name.'''
        self.name = name
        self.linkings = []
        self.info = {}

    def set_description(self, description):
        '''Describes the current room.'''
        self.description = description

    def link_room(self, room, wrld_side):
        '''Links the sides of the world, the current room and another room.'''
        self.neighbour = room
        self.wrld_side = wrld_side
        self.linkings.append(f'The {self.neighbour.name} is {self.wrld_side}')
        self.info[self.wrld_side] = self.neighbour

    def set_character(self, character):
        '''Connects the room with the character in it.'''
        self.character = character

    def get_details(self):
        '''Provides with information about the current room.'''
        print(self.name)
        print('--------------------')
        print(self.description)
        for link in self.linkings:
            print(link)

    def get_character(self):
        '''Gives the info about presence of characters in the room.'''
        try:
            return self.character
        except AttributeError:
            return None

    def set_item(self, item):
        '''Connects the room and the item in it.'''
        self.item = item

    def get_item(self):
        '''Gives the info about presence of items in the room.'''
        try:
            return self.item
        except AttributeError:
            return None

    def move(self, command):
        '''Is responsible for moving through rooms.'''
        if command in self.info:
            return self.info[command]
        return None

COUNTER = 0
class Character:
    '''A class to represent the character in different rooms.

    Attributes:
        name: str
            name of the character
        description: str
            info about the character
        message: str
            greetings from character

    '''

    message = ''

    def __init__(self, name, description):
        '''Inits Character with name and description.'''
        self.name = name
        self.description = description

    def set_conversation(self, message):
        '''Catches the message from the character.'''
        self.message = message

    def describe(self):
        '''Displays information about the character.'''
        print(f'{self.name} is here!')
        print(self.description)

    def talk(self):
        '''Starts the conversation with the character.'''
        print(f'[{self.name} says]: {self.message}')

class Enemy(Character):
    '''A class to represent the enemy character in different rooms.

    Attributes:
        name: str
            name of the enemy
        description: str
            info about the enemy
        message: str
            greetings from character
        weak_item: str
            the weakness of character

    '''

    weak_item = ''

    def set_weakness(self, weak_item):
        '''Shows the enemy`s weakness.'''
        self.weak_item = weak_item

    def fight(self, weapon):
        '''Checks if you can win the character with item or not.'''
        if weapon == self.weak_item:
            global COUNTER
            COUNTER += 1
            return True
        else:
            print(f'{self.name} crushes you, puny adventurer!')
            return False

    @staticmethod
    def get_defeated():
        '''Checks if all enemies are defeated.'''
        return COUNTER

class Ally(Character):
    '''A class to represent the ally character in different rooms.

    Attributes:
        name: str
            name of the ally
        description: str
            info about the ally
        message: str
            greetings from character

    '''

class Item:
    '''A class to represent the items in different rooms.

    Attributes:
        name: str
            name of the item
        description: str
            description of the item

    '''

    description = ''

    def __init__(self, name):
        '''Inits Item with name.'''
        self.name = name

    def set_description(self, description):
        '''Connects the item and its description.'''
        self.description = description

    def describe(self):
        '''Describes the item.'''
        print(f'The [{self.name}] is here - {self.description}')

    def get_name(self):
        '''Returns the name of the item.'''
        return self.name
