from blessed import Terminal
import blessed
from math import floor
import typing
import copy
import os, psutil
import utils

term = Terminal()

def main():
    with term.cbreak(): 
        #### EVERYTHING THAT NEEDS TO INITIALLIZED BEFORE ANYTHING ####
        borderHeightMax, borderWidthMax = term.height-2, term.width # the -2 in term.height is important so characters wont go over the border of the world, but this will only be required if you use tern.height (the whole screen)
        borderHeightMin, borderWidthMin = 0, 0
        # tracking the last time a chracter did something is usefull for a lot of tasks, like making collision detection more time efficient
        universalClock = 0
        #### EVERYTHING THAT NEEDS TO INITIALLIZED BEFORE ANYTHING ####

        exampleChar = utils.player("example character", 0, 0, universalClock, 1)

        while keyPressed.lower() != '\x1b':
            #### PRINT AREA ####
            print(term.clear())
            # isnt required depending on what game youre making.
            # also isnt required for simple games.
            utils.refreshScreen(strOfChar, xOfChars, yOfChars, amtOfEmptySpacesAtEveryLineOfCharacter)
            #### PRINT AREA ####

            # use timeout=0.01 for games where there actions that perform regardless of input for the game (for example: enemies in a platformer)
            # if actions are performed only when input by the user is given (for example an rts game) then dont put anything in timeout
            keyPressed = term.inkey()
            keyPressed = keyPressed.lower()

            universalClock = universalClock + 1

if __name__ == "__main__":
    main()
