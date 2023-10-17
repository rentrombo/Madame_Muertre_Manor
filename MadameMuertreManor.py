#Rowen Trombo 10/8/2023

#Madame Muertre's Manor
#Text adventure game
#answer key
# 1. Lady Beige, Poison, Coat, Dining Room \
# 2. Professor Forest, Impact, Eye Glasses, Stairwell \
# 3. Dr Blue, Poison, Brandy Glass, Lounge
# 4. Ms Crimson, Impact, Red Fingernail, Garden

#import modules
import re
import os
def error_y_n(y_n):
    invalid = True
    while invalid == True:
        y_n.lower()
        if y_n == 'y':
            answer = True
            invalid = False
        elif y_n == 'n':
            answer = False
            invalid = False
        else:
            y_n = input('Please try again. Acceptable commands are y or n.')
            invalid = True
            answer = False
    return answer
def user_format(input):
    return re.sub(r"[^a-zA-Z0-9]+", "", input.lower())

def game_end():
    print('You are wrong! The black abyss above quickly turns into blades and the darkness fills your vision until nothing is left.')
    print('You Have Died.')
    game_over = True
    os.system('cls')
    return game_over
def main():

    #This dictionary links a room to other rooms.
    rooms = {
            'Foyer': {'South': 'Stairwell'},
            'Stairwell': {'North': 'Foyer', 'South': 'Ballroom', 'East': 'Dining Room', 'West': 'Lounge', 'Clue': 'Eye Glasses'},
            'Lounge': {'South': 'Library', 'East': 'Stairwell', 'Clue': 'Brandy Glass'},
            'Library': {'North': 'Lounge', 'South': 'Study', 'East': 'Ballroom', 'Clue': 'Book'},
            'Study': {'North': 'Library', 'East': 'Conservatory', 'Clue': 'Invitations'},
            'Ballroom': {'North': 'Stairwell', 'South': 'Conservatory', 'East': 'Kitchen', 'West': 'Library', 'Clue': 'Bloody Ax'},
            'Conservatory': {'North': 'Ballroom', 'East': 'Patio', 'West': 'Study', 'Clue': 'Stethoscope'},
            'Patio': {'North': 'Kitchen', 'South': 'Garden', 'West': 'Conservatory', 'Clue': 'Broken Door Handle'},
            'Garden': {'North': 'Patio', 'Clue': 'Red Fingernail'},
            'Kitchen': {'North': 'Dining Room', 'South': 'Patio', 'West': 'Ballroom', 'Clue': 'Bloody Satin'},
            'Dining Room': {'South': 'Kitchen', 'West': 'Stairwell', 'East': 'Judgement Room', 'Clue': 'Coat'},
            'Judgement Room': {'West': 'Dining Room'}
        }
    #inspection dialogue
    item_description = {'Eye Glasses': { 1 : 'You see a shattered chandelier that looks like it was hanging from a rope pulley and was cut down.',
                                        2: 'Through the broken crystal pieces you see some glasses that look cracked from impact.',
                                        3: 'You see some red liquid on the upper corner of the frames…blood?',
                                        4: 'No, thank god! It looks like….pen? Who would use a red pen all the time?'},
                        'Coat': {1: 'A long table is set for 4 with a hunched over very average looking rich woman at the head of the table gray in the skin and very dead.',
                                2: 'All of the bowls are filled with mushroom soup except for the one in front of this woman which is totally empty.',
                                3: 'I see a beige fur coat draped around her as if by another, much more alive, person. Lady Beige, I presume?',
                                4: 'I see no blood on the coat and it doesn’t look like a struggle was made. Should I take this coat as evidence for my judgment?'},
                        'Brandy Glass': {1: 'Two red velvet chairs sit by a record player playing love songs with two snifter glasses on the table between them',
                                        2 : 'One glass is empty and smells moldy and made me feel light headed when I took a whiff, not something liqueur usually does to me.',
                                        3 : 'The other glass has a deep red lipstick imprint on it and smells of straight brandy. These glasses definitely held different substances.',
                                        4 : 'I notice the window is open and drag marks are going towards the back side of the house from it. Something big was being dragged. Maybe…a person?',
                                        5 : 'I think this musty smelling glass is the best clue I have, maybe I can figure out what this rancid smell is and why it has such an intense effect from just the smell.'},
                        'Book': {1:'The calmness of the books is juxtaposed by the mess that looks like it was made from everything being swept off of the desk that sits in the most lit part of the room.',
                                 2: 'The only thing still on it is a book on poisonous mushrooms. Open to a page on death cap mushrooms.',
                                 3: 'A red pen has circled different chemicals in the mushrooms that cause the poisonous death from consuming them.',
                                 4 : 'A single thigh high stocking lays across the armchair near the desk. I doubt anyone named ‘Lady Beige’ would wear such a thing.',
                                 5 : 'This book could serve useful in finding out what may have been used in these murders.'},
                        'Stethoscope': {1: 'It is as if I have stepped outside but the panes of glass all around me says differently.',
                                        2: 'Although the smell of the flora and fauna are invigorating there is something much harsher I am detecting as well.',
                                        3 : 'I look to my right and see a pile of cleaning supplies, bleach, plastic bags, mop that looks well used and some also stained red scrub brushes.',
                                        4: 'Weirdly enough, there is a stethoscope flung on top of everything. It looks clean but broken as if from too much strain. ',
                                        5 : 'It is knotted like it was tied around something as a sort of handle or pulling device.',
                                        6: 'Is this a doctors accomplice to one of our murders? What would be heavy enough to break a stethoscope?'},
                        'Bloody Ax' : {1: 'Wow the smell of bleach punches me in the face the moment I enter this room. Its cleanliness is reflected on the stark white marble covering the floor and walls.',
                                2: 'I see if I can see anything under any of the chairs when a glimmer comes from beneath the bandstand.',
                                3: 'Is that… an ax? I tug at the handle and a shining bloodied blade is halted before my face.',
                                4 : 'This seems to match one I saw hanging in the Stairwell. I did notice it looked like it should have been a pair.'},
                        'Bloody Satin' : {1: 'I see a pot of mushroom soup on the stove, the room looks disheveled as if someone was looking for an ingredient while panicking.',
                                          2: 'Hanging from the apron hooks are pieces of red satin, you can barely see it but they have red stains all over them. Could this be blood from one of the murders?',
                                          3: 'The fabric itself is a deep red almost, well... almost a crimson color.',
                                          4: 'Was someone wearing crimson cleaning up blood?'},
                        'Broken Door Handle' : {1: 'This room seems relatively untouched but the door leading to it is destroyed.',
                                                2: 'It looks like the lock was attempted to be picked by a red pen. Is this the same red pen from the glasses in the stairwell?',
                                                3: 'Ultimately the door handle screws were undone by a bobby pin.',
                                                4: 'Red pen and a bobby pin, someone who does mark ups often and a person with an innovative updo. Huh.'},
                        'Red Fingernail' : {1: 'This garden is quite bare and unkempt. The only notable areas being the well that is in the center of the foliage.',
                                            2: 'As I go up to give it a closer look, I see claw marks on the edge as if someone was trying to pull themselves out of the well',
                                            3: 'I look over the edge and see a red acrylic nail wedged in between the pieces of stone. Is she…did she...what a horrible way to go.',
                                            4: 'Now that I look down I see drag marks that go around to the side of the house right about where the Lounge is. ',
                                            5: 'This is no small thing being dragged, maybe that has something to do with the poor woman who fell down the well. I should take this nail as evidence.'},
                        'Invitations' : {1: 'My eye suddenly catches three invitations laying on the side table near the chaise lounge, neatly adorned with a soft silk bow.',
                                         2: 'One invitation is for Lady Beige, as to be expected. One is for a Professor Forest, and the last is addressed to Dr. Blue and Ms.Crimson.',
                                         3: 'Hmmm, a couple?',
                                         4: "I wonder if a lovers' feud had anything to do with our murders, certainly would be an oppportunity at this remote manor.",
                                         5: 'Thank goodness I found these, now I know I am trying to solve 4 murders. Order in which they died, how they died, where they died and evidence to prove it.',
                                         6: 'Got it!'}
    }
    #list for final boss fight
    guest = ['ladybeige', 'professorforest', 'drblue', 'mscrimson']
    death_by = ['poison', 'impact', 'poison', 'impact']
    evidence = ['coat','eyeglasses', 'brandyglass', 'redfingernail']
    murder_rooms = ['diningroom', 'stairwell', 'lounge', 'garden']
    inventory = []

    #opening menu
    print("Madame Muertre's Mansion")
    print('You have been sent an invitation to the home of Madame Meurtre to solve a crime.')
    print(' A letter from this mysterious woman told you a tragedy has occurred and she needs your expertise to solve it. ')
    print(' She sent you the address and covered all of your travel expenses so there was nothing stopping you from going.')
    print('')
    print('Once arriving in the Foyer of the Manor, you find a note.')
    print('The note said that this, Madame Meurtre, was trying to rid herself of her nemesis Lady Beige by poisoning her meal at a dinner party')
    print('and needed the other guests to ensure the element of surprise ... but things got out of hand and all 4 of them died.')
    print('She needs you to solve who was killed in what order, how they died, where they died and provide the evidence you have for your claims.')
    print('Only then will you receive your freedom, otherwise yours will be the next murder to be solved!')
    print('You have until dawn, when you think you know, go to my portrait in the Dining Room and say the following words...')
    print('If I have lost, I have lost.')
    print('you MUST pickup all items before facing your Judgement, or you will have lost.')
    print('Good luck.')

    #print controls
    print('Move from room to room to find clues.')
    print('Move commands: go South, go North, go East, go West, inspect, inventory, or hint')
    #nested functions
    def move(direction):
        room_directory = rooms.get(current_room)
        new_room = room_directory.get(direction, error_move)
        return new_room

    def inspect(item):
        room_directory = rooms.get(current_room)
        inspect_item = room_directory.get(item, error_inspect)
        return inspect_item

    def inventory_add(inspect_item, inventory):
        if inspect_item in inventory:
            inventory_y_n = input('There is nothing in this room. Do you want to look in your inventory? y/n ')
            inventory_open = error_y_n(inventory_y_n)
            if inventory_open == True:
                print('Your Inventory: ', inventory)
            else:
                inventory_open = False
        else:
            dialogue = item_description.get(inspect_item, error_inspect)
            for i in range(1, len(dialogue) + 1):
                print(dialogue.get(i))
            inventory_y_n = input('Do you want to add '+ inspect_item + ' to your inventory? y/n ')
            inventory_item = error_y_n(inventory_y_n)
            if inventory_item == True:
                inventory = inventory.append(inspect_item)
            else:
                inventory_item = False
    # set players current room to Foyer
    current_room = 'Foyer'
    move_direction = ''
    #set error message
    error_move = "---------You can't go that way!-----------"
    error_inspect = "------------You can't do that!--------------"
    #loop
    while move_direction != 'exit':
    #display current room
        print("_________________________________________")
        print('You are in the', current_room)
        if current_room == 'Judgement Room':
           #INPUT to complete game
            final = error_y_n(input('Are you sure you have solved the murders?(y / n)'))
            if final == True and len(inventory) == 10:
                print('You say, ‘IF I HAVE LOST, I HAVE LOST.’ And the large portrait of Madame Muertre releases from the wall entering you into a small room of all mirrors.\n' 
                'The ceiling is a dark abyss filled with what you assume is your impending death if you have not solved these murders')
                print('The first to die was of course Lady Beige.')
                for i in range(0,4):
                    game_over = False
                    if i == 0:
                        dead_guest = 'ladybeige'
                    else:
                        dead_guest = input('Who died next?')
                        dead_guest = user_format(dead_guest)
                        if dead_guest != guest[i]:
                            game_over = game_end()
                            break
                        else:
                            print('Correct.')
                            game_over = False
                    death = input('And how did they die? Poison or Impact?')
                    death = user_format(death)
                    if death != death_by[i]:
                        game_over = game_end()
                        break
                    else:
                        print('Correct...')
                        game_over = False
                        found_evidence = input('What evidence did you find for that?')
                        found_evidence = user_format(found_evidence)
                        if found_evidence != evidence [i]:
                            game_over = game_end()
                            break
                        else:
                            print('Correct.....')
                            game_over = False
                            death_room = input('What room did this occur in? The...')
                            death_room = user_format(death_room)
                            if death_room != murder_rooms[i]:
                                game_over = game_end()
                                break
                            else:
                                print('Correct, hm...')
                                game_over = False
                if game_over == True:
                    break
                else:
                    print('Congratulations. You solved it!')
                    print('The mirror in front of you opens and you are blinded by light.')
                    print('You walk forward just happy to be out of that Murder Manor.')
                    print('You find yourself on a sunny grassy hill. You spot your car and safely jump inside.')
                    print('You did it, you are out.')
                    break
            else:
                game_end()
                break
    # get direction input
        move_direction = input('Enter your move: ')
        #use move function to look up in dictionary for next room
        if move_direction == 'go South':
            if move('South') == error_move:
                print(error_move)
            else:
                current_room = move('South')
        elif move_direction == 'go North':
            if move('North') == error_move:
                print(error_move)
            else:
                current_room = move('North')
        elif move_direction == 'go East':
            if move('East') == error_move:
                print(error_move)
            else:
                current_room = move('East')
        elif move_direction == 'go West':
            if move('West') == error_move:
                print(error_move)
            else:
                current_room = move('West')
        #output for invalid entries
        elif move_direction == 'inspect':
            if inspect('Clue') == error_inspect:
                print(error_inspect)
            else:
                inventory_add(inspect('Clue'), inventory)
        elif move_direction == 'hint':
            print('The room in which you find the clue can be assumed as the room in which the guest died.')
        elif move_direction == 'inventory':
            print('You have: ' + str(inventory))
        else:
            print('Please try again.')
            print('Move commands: go South, go North, go East, go West, inspect, inventory and hint')
    #statement for game end
    print('Thank you for playing. You have exited the game.')




main()