'''module with classes for the main game module'''


class Stage:
    '''A class to represent the stage and info about it.

    Attributes:
        name: str
            name of the stage
        description: str
            description of the stage
        neighbour: Stage
            the following stage
        way: str
            forward, back, left, right
        character: Character
            character in the stage
        item: Item
            item in the stage
        linkings: list
            list with str about connected stages and ways
        info: dict
            dict with neighbours as values and ways as keys

    '''

    description = ''
    neighbour = None
    way = ''
    enemy = None
    ally = None
    item = None

    def __init__(self, name):
        '''Inits Stage with name.'''
        self.name = name
        self.linkings = []
        self.info = {}

    def set_description(self, description):
        '''Describes the current stage.'''
        self.description = description

    def link_stage(self, room, way):
        '''Links the way, the current stage and another stage.'''
        self.neighbour = room
        self.way = way
        self.linkings.append(f'The {self.neighbour.name} is {self.way}')
        self.info[self.way] = self.neighbour

    def set_enemy(self, enemy):
        '''Connects the stage with the enemy in it.'''
        self.enemy = enemy

    def set_ally(self, ally):
        '''Connects the stage with the ally in it.'''
        self.ally = ally

    def get_details(self):
        '''Provides with information about the current stage.'''
        print(self.name)
        print('--------------------')
        print(self.description)
        for link in self.linkings:
            print(link)

    def get_enemy(self):
        '''Gives the info about presence of enemies in the stage.'''
        try:
            return self.enemy
        except AttributeError:
            return None

    def get_ally(self):
        '''Gives the info about presence of allies in the stage.'''
        try:
            return self.ally
        except AttributeError:
            return None

    def set_item(self, item):
        '''Connects the stage and the item in it.'''
        self.item = item

    def get_item(self):
        '''Gives the info about presence of items in the stage.'''
        try:
            return self.item
        except AttributeError:
            return None

    def move(self, command):
        '''Is responsible for moving through stages.'''
        if command in self.info:
            return self.info[command]
        return None

class Character:
    '''A class to represent the character in different stages.

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
        print(f'Here is: {self.name}')
        print(self.description)

FIGHT_COUNTER = 0

class Enemy(Character):
    '''A class to represent the enemy character in different stages.

    Attributes:
        name: str
            name of the enemy
        description: str
            info about the enemy
        message: str
            greetings from enemy
        weak_item: str
            the weakness of enemy

    '''

    weak_item = ''

    def set_weakness(self, weak_item):
        '''Shows the enemy`s weakness.'''
        self.weak_item = weak_item

    def fight(self, weapon):
        '''Checks if you can win the character with item or not.'''
        if weapon == self.weak_item:
            global FIGHT_COUNTER
            FIGHT_COUNTER += 1
            return True
        else:
            print(f'You can`t do anything with it for {self.name}!')
            return False

    @staticmethod
    def get_defeated():
        '''Checks if all enemies are defeated.'''
        return FIGHT_COUNTER

class Ally(Character):
    '''A class to represent the ally character in different stages.

    Attributes:
        name: str
            name of the ally
        description: str
            info about the ally
        message: str
            greetings from character

    '''

    help_item = ''

    def talk(self):
        '''Starts the conversation with the character.'''
        print(f'[{self.name} says]: {self.message}')

    def set_helper(self, help_item):
        '''Connects the ally and help_item.'''
        self.help_item = help_item
    
    def help_provider(self):
        '''Provides help for the mh.'''
        try:
            return self.help_item
        except AttributeError:
            return None

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
