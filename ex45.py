# You Make a Game
from sys import exit
from random import randint

KEY1 = 0
KEY2 = 0
BEFORE = None

class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n----------------"
            scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(scene_name)

## rooms
class Death(object):
    quips = {
        "You died. Try next time to do better.",
        "You're so stupid!",
        "Such a loser!"
    }
    def enter(self):
        print Death.quips[randint(0, len(self.quips)-1)]
        print "Play agan? [Y/N]"
        do = raw_input("> ")
        if (do.upper() == "Y"):
            return 'init_room'
        else:
            exit(1)

class KeyRoom(object):
    def enter(self):
        global KEY1
        global BEFORE
        BEFORE = 'key_room'
        print "You entered this room and find that there is a key."
        print "1.Take the key and go back  2.Leave it and go back[1/2]"
        do = raw_input("> ")
        if (do == "1"):
            KEY1 = 1
            return 'verse_room'
        else:
            return 'verse_room'

class VerseRoom(object):
#    global BEFORE
    def enter(self):
        global BEFORE
        print BEFORE
        print "Before you enter this room. You must answer a question:"
        print "Where there is a will,____________. Please fill the blank."
        print "You only have three chances."
        right_answer = "there is a way"

        answer = raw_input("> ").lower().strip()
        counts = 1
        while (answer != right_answer and counts < 3):
            print "keep trying! You have %d chance" %(3-counts)
            answer = raw_input("> ").lower().strip()
            counts += 1

        if(answer == right_answer):
            print "Good job! You are in this room. There is another door on the opposite wall."
            while True:
                print "1.Open the door  2.Go back [1/2]"
                do = raw_input("> ")
                if (do == "1"):
                    if(BEFORE == 'init_room'):
                        return 'key_room'
                    else:
                        return 'init_room'
                elif(do == "2"):
                    return BEFORE
                else:
                    pass
        else:
            print "Bomb!!! You failed."
            return 'death'


class InitRoom(object):

    def enter(self):
        global BEFORE
        BEFORE = 'init_room'
        print BEFORE
        print "There are three doors on different wall. "
        print "Which one will you open ? 1, 2 or 3?"

        room_no = raw_input("> ")
        while(room_no not in ["1", "2", "3"]):
            print "Please input 1, 2, or 3"
            room_no = raw_input("> ")

        if (room_no == "1"):
            return 'verse_room'
        elif (room_no == "2"):
            return 'math_room'
        else:
            return 'history_room'

class HistoryRoom(object):
    def enter(self):
        print "Before you enter this room, there is a question for you: "
        print "which year was people's republic of China built?"
        answer = raw_input("> ")

        if(answer == "1949"):
            print "Now you entered this room and there are nothing."

            do = "N"
            while (do.upper() != "Y"):
                print "It seems the wrong way. Go back? [Y/N]"
                do = raw_input("< ")

            return 'init_room'

        else:
            return 'history_room'




class MathRoom(object):
    def enter(self):
        print "Before you enter this room, there is a question for you: 3 + 5 = ?"
        answer = raw_input("> ")

        counts = 1 # times of answer
        while(answer != "8" and counts < 3):
            print "wrong answer! You have %d chance" %(3-counts)
            answer = raw_input("> ")
            counts = counts + 1

        if(answer == "8"):
            print "Now you entered this room. There is a door on your right."

            do = "N"
            while True:
                print "1.Go back 2.Open the door. [1/2]"
                do = raw_input("< ")
                if (do == "1"):
                    return 'init_room'
                elif (do == "2"):
                    print "The door is locked. Maybe you need a key."
                    if (KEY1 == 0):
                        print "You don't have a key."
                    else:
                        print "You've got a key before. You used it and the door is open."
                        return 'pic_room'
                else:
                    pass


class PicRoom(object):
    def enter(self):
        global KEY2
        print "There is a poster of JAY on the wall and a keypad lock on the box."
        print "Besides, there is a door on your left."
        choise = "99" # initialize
        while (choise not in ["1", "2"]):
            print "1.Open the door  2.Walk to the box"
            choise = raw_input("< ")

        if (choise == "1"):
            return 'last_room'

        elif (choise == "2" and KEY2 == 0):
            print "the code is 4 digits. You only have three chances."
            code = "0118"
            guess = raw_input("[keypad]> ")
            counts = 1

            while (guess != code and counts < 3):
                print "You only have %d chance." %(3-counts)
                guess = raw_input("[keypad]> ")
                counts += 1

            if (guess == code):
                print "Correct! The box is open and there is a key."
                print "1.Take the key 2.Leave it [1/2]"
                do = raw_input("> ")
                if(do == "1"):
                    KEY2 = 1
                    return 'pic_room'
            else:
                print "Bomb! You've ran out your chance."
                return 'death'

        else:
            print "You've looked for the box before."
            return 'pic_room'


class LastRoom(object):
    def enter(self):
        print "There is only a door in this room. You try to open the door,"
        print "but it seems to be locked. Maybe you need a key."
        if (KEY2 == 0):
            print "You've got a key before."
            print "1.Use it  2.Not use and go back to the last room.[1/2]"
            use = raw_input("> ")
            if(use == "1"):
                print "You still can't open the door. It's not the right key!"
                print "Go back to the last room to find more clues? [Y/N]"
                do = raw_input("> ")
                if (do.upper() == "Y"):
                    return 'pic_room'
                else:
                    return 'last_room'
            else:
                return 'pic_room'
        else:
            print "You've got two keys. You tried them and the door is open."
            print "Oh!!! You are saved. You successfully run out of this place!"
            exit(1)

class Map(object): # a map stores all scenes
    rooms = {
        'death': Death(),
        'key_room': KeyRoom(),
        'verse_room': VerseRoom(),
        'init_room': InitRoom(),
        'history_room': HistoryRoom(),
        'math_room':MathRoom(),
        'pic_room':PicRoom(),
        'last_room': LastRoom()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        return Map.rooms.get(scene_name)

    def opening_scene(self):
        print "-----------------"
        print "Your are wake at a room you've never been to. "
        return self.next_scene(self.start_scene)


# a_map = Map('init_room')
# a_game = Engine(a_map)
# a_game.play()
