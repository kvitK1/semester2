'''the plot of the game'''

import game


entry = game.Stage('Entry to the forest')
entry.set_description('A deep and quite dark forest, full of high trees.')

path = game.Stage('Path')
path.set_description('A narrow path with big bushes on both sides')

lawn = game.Stage('Lawn')
lawn.set_description('A small lawn, filled with a sweet floral aroma.')

pond = game.Stage('Pond')
pond.set_description('A pond with little fish in it.')

cave = game.Stage('Cave')
cave.set_description('A deep dark cave, something scary could live inside..')

entry.link_stage(path, 'north')
path.link_stage(entry, 'south')
path.link_stage(pond, 'east')
path.link_stage(lawn, 'west')
pond.link_stage(path, 'south')
lawn.link_stage(path, 'south')
path.link_stage(cave, 'north')
cave.link_stage(path, 'south')

slime = game.Enemy('Slime', 'A green and jumpy slimy creature, how can one stop it?')
slime.set_conversation('*Chew...* *chew...*')
slime.set_weakness('snowball')

bear = game.Enemy('Bear', 'Wow, it`s big and hungry!')
bear.set_conversation('*Rooooarr*')
bear.set_weakness('honey')

mermaid = game.Enemy('Mermaid', 'A beautiful creature with killing voice.')
mermaid.set_conversation('Aha, aha, hahaha, hahaha-ha\n\
Brlrlrl... a a a\nBrlrl, brlrl, haha\nA a a, a a a, a a a, a-a-a\n\
Aha, aha, hahaha, hahaha-ha\nBrlrlrl... a a a\nBrlrl, brlrl, haha')
mermaid.set_weakness('headphones')

wasp = game.Enemy('Wasp', 'Much bigger than the ordinary one..')
wasp.set_conversation('*Bazzzz*')
wasp.set_weakness('peppermint')

evil_spirit = game.Enemy('Evil Spirit', 'What a scary monster..')
evil_spirit.set_conversation('You won`t leave this cave anymore!')
evil_spirit.set_weakness('puzzle')

snowball = game.Item('snowball')
snowball.set_description('a small, but freezing thing.')

honey = game.Item('honey')
honey.set_description('sweet and sticky.')

headphones = game.Item('headphones')
headphones.set_description('they mute the sound completely.')

peppermint = game.Item('peppermint')
peppermint.set_description('smells odd.')

puzzle = game.Item('puzzle')
puzzle.set_description('something strange is written on it.')

yellow_spirit = game.Ally('Yellow Spirit of the Forest',\
    'One of the three forest spirits, which cares for all the trees and green grass.')
yellow_spirit.set_conversation('Please, help us! This item will help you on your way.')
yellow_spirit.set_helper(headphones)

red_spirit = game.Ally('Red Spirit of the Forest',\
    'One of the three forest spirits. It cares for all the animals in the forest.')
red_spirit.set_conversation('Help us! Take this, it might be helpful if someone is on your way.')
red_spirit.set_helper(peppermint)

path.set_item(snowball)
entry.set_ally(red_spirit)
cave.set_ally(yellow_spirit)
entry.set_enemy(slime)
path.set_enemy(wasp)
pond.set_enemy(mermaid)
lawn.set_enemy(bear)

current_stage = entry
backpack = []

DEAD = False
HP = 4
while HP!=0:

    print('\n')
    current_stage.get_details()

    friend = current_stage.get_ally()
    if friend is not None:
        friend.describe()

    bad = current_stage.get_enemy()
    if bad is not None:
        bad.describe()

    item = current_stage.get_item()
    if item is not None:
        item.describe()

    command = input('> ')

    if command in ['north', 'south', 'east', 'west']:

        prev_stage = current_stage
        stage_move = current_stage.move(command)
        if stage_move is not None:
            current_stage = stage_move
        else:
            current_stage = prev_stage
    elif command == 'talk':
        if friend is not None:
            friend.talk()
            help_item = friend.help_provider()
            backpack.append(help_item.name)
            print(f'You`ve got {help_item.name} in your backpack!')
            current_stage.ally = None
        if bad is not None:
            print(f'[{bad.name} says]: {bad.message}')

    elif command == 'fight':
        if bad is not None:
            print(f'[{bad.name} says]: {bad.message}')
            print(f'Your HP level: {HP}.')
            print('What will you fight with?')
            print('['+ ', '.join(backpack) + ']')
            fight_with = input()

            if fight_with in backpack:

                if bad.fight(fight_with) is True:
                    print('Yay, you won the fight!')
                    print('You received a piece of puzzle.')
                    current_stage.enemy = None
                    backpack.remove(fight_with)
                    if current_stage == pond and current_stage.enemy is None:
                        pond.set_item(honey)
                    if bad.get_defeated() == 4:
                        print('\nYou`ve got all the pieces of the puzzle!\nHere you are...\n\
It might help you later.')
                        backpack.append(puzzle.name)
                        cave.set_enemy(evil_spirit)
                        print('\n---teleportation---\n')
                        current_stage = cave
                        current_stage.get_details()
                        current_stage.enemy.describe()
                        print(f'[Evil Spirit says]: {current_stage.enemy.message}')
                        print(f'Your HP level: {HP}.')
                        print('Are you ready to fight? (yes/no)')
                        BOL = True

                        while BOL is True:
                            answer = input('> ')
                            if answer == 'yes':
                                if HP > 2:
                                    print('Choose the item from your backpack:')
                                    print('['+ ', '.join(backpack) + ']')
                                    weapon = input()
                                    if current_stage.enemy.fight(weapon) is True:
                                        print('Something strange`s going on..')
                                        print('*covering of the monster cracks, blue light is about to get out*')
                                        contin = input('press anything to continue..')
                                        print('Thank you, a brave adventurer!\n\
I`m Blue Spirit of the Forest, last of three forest overseers.\
I take care of all the ponds, lakes and rivers.')
                                        print('You saved me from the impact of the witch`s maleficent magic.')
                                        print('You did a lot, now I`ll help you to find your way from the forest')
                                        contin = input('press anything to continue..')
                                        print('CONGRATULATIONS! Thank your for playing :3')
                                        HP=0
                                    else:
                                        print('Oh dear, you lost the fight.')
                                        HP-=1
                                    BOL = False
                                else:
                                    print('You don`t have enough health, sorry >_<')
                                    HP=0
                                    BOL = False
                            if answer == 'no':
                                print('Oh dear, you refused to fight.\
After some period of time you were killed by the Evil Spirit of this forest.\
The story of one more adventurer has finished...')
                                print('That\'s the end of the game.')
                                HP=0
                                BOL = False
 
                else:
                    print('Oh dear, you lost the fight.')
                    HP-=1

            else:
                print(f'You don\'t have a  {fight_with}.')

        else:
            print('There is no one here to fight with.')

    elif command == 'take':
        if item is not None:
            print(f'You put the {item.get_name()} in your backpack.')
            backpack.append(item.get_name())
            current_stage.set_item(None)
        else:
            print("There's nothing here to take!")

    else:
        print(f'I don\'t know how to {command}.')
print('That\'s the end of the game.')
