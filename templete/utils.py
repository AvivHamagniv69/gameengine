from blessed import Terminal
import blessed
from math import floor
import typing
import copy
import os, psutil

term = Terminal()

class player:
    def moveCharByItsSpeed(arrOfPos: list[int], SpeedOfChars: int, universalClock: int, plusOrMinus: bool) -> list[list[int], int]:
        '''
        moveCharByItsSpeed(list[int], int, int, bool) -> list[int], int
        moves the character on a chosen grid up or down/left or right
        '''
        if arrOfPos == -1:
            return arrOfPos, 0

        if plusOrMinus == False:
            for repos in range(len(arrOfPos)):
                arrOfPos[repos] -= SpeedOfChars

        else:
            for repos in range(len(arrOfPos)):
                arrOfPos[repos] += SpeedOfChars
        
        return arrOfPos, universalClock

    def moveCharToASpesificPoint(pointToMoveX: int, pointToMoveY: int, actualSprite: str, amtOfEmptySpacesPerLine: list[int] = None) -> list[list[int], list[int]]:
        '''
        moveCharToASpesificPoint(int, int, str, list[int] = None) -> list[int], list[int]
        give the function a starting point for x and y and it returns its new position
        '''
        if actualSprite == -1:
            return allCoorsOfCharX, allCoorsOfCharY

        allCoorsOfCharX = []
        allCoorsOfCharY = []
        spriteSplitedByLines = actualSprite.split("\n")
        tempPointToMoveX = pointToMoveX

        for line in range(len(spriteSplitedByLines)):
            listOfLineOfSpirte = list(spriteSplitedByLines[line])
            if amtOfEmptySpacesPerLine != None:
                pointToMoveX = tempPointToMoveX + amtOfEmptySpacesPerLine[line]

            for eachPoint in range(len(listOfLineOfSpirte)):
                allCoorsOfCharX.append(eachPoint+pointToMoveX)
                allCoorsOfCharY.append(pointToMoveY)
            pointToMoveY += 1

        return allCoorsOfCharX, allCoorsOfCharY

    def takeOutEmptySpaces(sprite: str) -> list[str, list[int]]:
        '''
        takeOutEmptySpaces(str) -> str, list[int]
        takes out all the empty spaces at the start of each line of the sprite and places the amount of them in an array for each line.
        '''
        if sprite == -1:
            return -1, -1

        amtOfEmptySpaces = []
        toCombineTogether = []
        spriteSplitedByLines = sprite.split("\n")
        firstCharOfLine = 0
        for line in range(len(spriteSplitedByLines)):
            amtOfEmptySpaces.append(0)
            listOfLine = list(spriteSplitedByLines[line])
            if listOfLine[0] == ' ':
                while listOfLine[0] == ' ':
                    amtOfEmptySpaces[line] += 1
                    listOfLine.pop(0)

            toCombineTogether.append(''.join(listOfLine)+"\n")
            firstCharOfLine += len(listOfLine)

        toCombineTogether = ''.join(toCombineTogether)
        toCombineTogether = list(toCombineTogether)
        toCombineTogether.pop(len(toCombineTogether)-1)
        toCombineTogether = ''.join(toCombineTogether)
        
        return toCombineTogether, amtOfEmptySpaces

    def __init__(self, sprite, startingPointOfX, startingPointOfY, universalClock, speedOfChar):
        self.spriteWithoutEmptySpacesAtTheStart, self.amtOfEmptySpacesPerLine = takeOutEmptySpaces(sprite)
        self.allCoorsOfCharX, self.allCoorsOfCharY = moveCharToASpesificPoint(startingPointOfX, startingPointOfY, self.spriteWithoutEmptySpacesAtTheStart)
        self.lastTickMoved = universalClock
        self.speedOfChar = speedOfChar

    def moveRight(self, charToMoveRight, keyPressed, universalClock):
        if keyPressed == charToMoveRight:
            self.allCoorsOfCharX, self.lastTickMoved = moveCharByItsSpeed(self.allCoorsOfCharX, self.speedOfChar, universalClock, plusOrMinus=True)
        return self.allCoorsOfCharX, self.lastTickMoved

    def moveLeft(self, charToMoveLeft, keyPressed, universalClock):
        if keyPressed == charToMoveLeft:
            self.allCoorsOfCharX, self.lastTickMoved = moveCharByItsSpeed(self.allCoorsOfCharX, self.speedOfChar, universalClock, plusOrMinus=False)
        return self.allCoorsOfCharX, self.lastTickMoved

    def moveDown(self, charToMoveDown, keyPressed, universalClock):
        if keyPressed == charToMoveDown:
            self.allCoorsOfCharY, self.lastTickMoved = moveCharByItsSpeed(self.allCoorsOfCharY, self.speedOfChar, universalClock, plusOrMinus=True)
        return self.allCoorsOfCharX, self.lastTickMoved


















def allLatestMovingChars(allClocks: list[int]) -> list[int]:
    '''
    allLatestMovingChars(list[int]) -> list[int]
    returns all the characters that moved recently
    '''
    localAllClocks = copy.copy(allClocks)
    checkOn = localAllClocks.index(max(localAllClocks))
    allObjsToCheck = [checkOn]
    localAllClocks.pop(checkOn)
    for moreObjs in range(len(localAllClocks)):
        if checkOn in localAllClocks:
            allObjsToCheck.append(localAllClocks.index(checkOn))
            localAllClocks.pop(allObjsToCheck[len(allObjsToCheck)-1])
        else:
            break

    return allObjsToCheck

def moveCharToASpesificPoint(pointToMoveX: int, pointToMoveY: int, actualSprite: str, amtOfEmptySpacesPerLine: list[int] = None) -> list[list[int], list[int]]:
    '''
    moveCharToASpesificPoint(int, int, str, list[int] = None) -> list[int], list[int]
    give the function a starting point for x and y and it returns its new position
    '''
    if actualSprite == -1:
        return allCoorsOfCharX, allCoorsOfCharY

    allCoorsOfCharX = []
    allCoorsOfCharY = []
    spriteSplitedByLines = actualSprite.split("\n")
    tempPointToMoveX = pointToMoveX

    for line in range(len(spriteSplitedByLines)):
        listOfLineOfSpirte = list(spriteSplitedByLines[line])
        if amtOfEmptySpacesPerLine != None:
            pointToMoveX = tempPointToMoveX + amtOfEmptySpacesPerLine[line]

        for eachPoint in range(len(listOfLineOfSpirte)):
            allCoorsOfCharX.append(eachPoint+pointToMoveX)
            allCoorsOfCharY.append(pointToMoveY)
        pointToMoveY += 1

    return allCoorsOfCharX, allCoorsOfCharY

def moveCharByItsSpeed(arrOfPos: list[int], SpeedOfChars: int, universalClock: int, plusOrMinus: bool) -> list[list[int], int]:
    '''
    moveCharByItsSpeed(list[int], int, int, bool) -> list[int], int
    moves the character on a chosen grid up or down/left or right
    '''
    if arrOfPos == -1:
        return arrOfPos, 0

    if plusOrMinus == False:
        for repos in range(len(arrOfPos)):
            arrOfPos[repos] -= SpeedOfChars

    else:
        for repos in range(len(arrOfPos)):
            arrOfPos[repos] += SpeedOfChars
    
    return arrOfPos, universalClock

def actualCheckIfCollsion(xOfChars: list[list[int]], yOfChars: list[list[int]], posOfCharOnArr1: int, posOfCharOnArr2: int, firstCoorOfLine: int, lastCoorOfLine: int) -> bool:
    '''
    actualCheckIfCollsion(list[list[int]], list[list[int]], int, int, int, int) -> bool
    checks if a line of the first character collides with the second character
    '''
    if xOfChars[posOfCharOnArr1][firstCoorOfLine] in xOfChars[posOfCharOnArr2] or xOfChars[posOfCharOnArr1][lastCoorOfLine] in xOfChars[posOfCharOnArr2]:
        if yOfChars[posOfCharOnArr1][firstCoorOfLine] in yOfChars[posOfCharOnArr2] or yOfChars[posOfCharOnArr1][lastCoorOfLine] in yOfChars[posOfCharOnArr2]:
            return True
    
    return False

def checkCollisionPerLine(xOfChars: list[list[int]], yOfChars: list[list[int]], posOfCharOnArr1: int, posOfCharOnArr2: int, strOfChar: list[str]) -> bool:
    '''
    checkCollisionPerLine(list[list[int]], list[list[int]], int, int, list[str]) -> bool
    checks if all the lines in one character (posOfCharOnArr1) collides with another character (posOfCharOnArr2), if they are returns True
    '''
    spriteSplitedByLines = strOfChar[posOfCharOnArr1].split("\n")
    firstCoorOfLine = 0
    lastCoorOfLine = len(spriteSplitedByLines[0])-1

    for checkPerLine in range(len(spriteSplitedByLines)):
        if actualCheckIfCollsion(xOfChars, yOfChars, posOfCharOnArr1, posOfCharOnArr2, firstCoorOfLine, lastCoorOfLine):
            return True

        firstCoorOfLine += len(spriteSplitedByLines[checkPerLine])
        if checkPerLine < len(spriteSplitedByLines)-1:
            lastCoorOfLine += len(spriteSplitedByLines[checkPerLine+1])

def CheckCollision(xOfChars: list[list[int]], yOfChars: list[list[int]], allClocks: list[int], lastButtonUsed: list[str], SpeedsOfChars: list[int], strOfChar: list[str]) -> list[list[list[int]], list[list[int]]]:
    '''
    CheckCollision(list[list[int]], list[list[int]], list[int], list[str], list[int], list[str]) -> list[list[list[int]], list[list[int]]]
    takes all the characters that moved in this tick and checks if they hit another objects, if they do it returns them to their previous positions.
    '''
    allObjsToCheck = allLatestMovingChars(allClocks)

    for obj in range(len(allObjsToCheck)):
        for index in range(len(xOfChars)):
            # we dont want to check the same character against itself
            if index == allObjsToCheck[obj] or strOfChar[index] == -1 or strOfChar[allObjsToCheck[obj]] == -1:
                continue

            if checkCollisionPerLine(xOfChars, yOfChars, allObjsToCheck[obj], index, strOfChar):
                xTemp = xOfChars[allObjsToCheck[obj]]
                yTemp = yOfChars[allObjsToCheck[obj]]

                # this section finds the last coordinets of all of the points of the character
                if lastButtonUsed[allObjsToCheck[obj]] == 'd':
                    xTemp = moveCharByItsSpeed(xOfChars[allObjsToCheck[obj]], SpeedsOfChars[allObjsToCheck[obj]], False)

                elif lastButtonUsed[allObjsToCheck[obj]] == 'a':
                    xTemp = moveCharByItsSpeed(xOfChars[allObjsToCheck[obj]], SpeedsOfChars[allObjsToCheck[obj]], True)

                elif lastButtonUsed[allObjsToCheck[obj]] == 'w':
                    yTemp = moveCharByItsSpeed(yOfChars[allObjsToCheck[obj]], SpeedsOfChars[allObjsToCheck[obj]], True)

                elif lastButtonUsed[allObjsToCheck[obj]] == 's':
                    yTemp = moveCharByItsSpeed(yOfChars[allObjsToCheck[obj]], SpeedsOfChars[allObjsToCheck[obj]], False)

                for turnIntoIterable in range(len(xOfChars[allObjsToCheck[obj]])):
                    xOfChars[allObjsToCheck[obj]][turnIntoIterable] = xTemp[turnIntoIterable]
                    yOfChars[allObjsToCheck[obj]][turnIntoIterable] = yTemp[turnIntoIterable]

    return xOfChars, yOfChars

def refreshScreen(actualChar: list[str], xOfChars: list[list[int]], yOfChars: list[list[int]], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]], term=term):
    '''
    refreshScreen(list[str], list[list[int]], list[list[int]], list[list[int]])
    prints all the characters on the screen line by line.
    '''
    for refresh in range(len(actualChar)):
        if actualChar[refresh] == -1:
            continue

        lineOfChar = actualChar[refresh].split("\n")
        PointToPrintAt = 0
        for line in range(len(lineOfChar)):
            print(term.move_xy(xOfChars[refresh][PointToPrintAt], yOfChars[refresh][PointToPrintAt])+lineOfChar[line])
            PointToPrintAt += len(lineOfChar[line])

def moveCharByKey(arrOfCharOnAxis: list[int], speedOfChar: int, keyPressed: str, buttonToRemove: str, buttonToAdd: str, universalClock: int, lastButtonUsed: str) -> list[list[int], int, str]:
    '''
    moveCharByKey(list[int], int, str, str, str, int) -> list[int], int, str
    moveCharByKey(arrOfCharOnAxis, speedOfChar, keyPressed, buttonToRemove, buttonToAdd, universalClock) -> arrOfCharOnAxis, universalClock, keyPressed
    moves the character by its speed depending on the button pressed.
    '''
    if keyPressed != buttonToAdd and keyPressed != buttonToRemove:
        return arrOfCharOnAxis, 0, lastButtonUsed

    else:
        if keyPressed == buttonToAdd:
            arrOfCharOnAxis, lastButtonUsed = moveCharByItsSpeed(arrOfCharOnAxis, speedOfChar, universalClock, plusOrMinus = True)

        if keyPressed == buttonToRemove:
            arrOfCharOnAxis, lastButtonUsed = moveCharByItsSpeed(arrOfCharOnAxis, speedOfChar, universalClock, plusOrMinus = False)
        
        return arrOfCharOnAxis, universalClock, keyPressed

def takeOutEmptySpaces(sprite: str) -> list[str, list[int]]:
    '''
    takeOutEmptySpaces(str) -> str, list[int]
    takes out all the empty spaces at the start of each line of the sprite and places the amount of them in an array for each line.
    '''
    if sprite == -1:
        return -1, -1

    amtOfEmptySpaces = []
    toCombineTogether = []
    spriteSplitedByLines = sprite.split("\n")
    firstCharOfLine = 0
    for line in range(len(spriteSplitedByLines)):
        amtOfEmptySpaces.append(0)
        listOfLine = list(spriteSplitedByLines[line])
        if listOfLine[0] == ' ':
            while listOfLine[0] == ' ':
                amtOfEmptySpaces[line] += 1
                listOfLine.pop(0)

        toCombineTogether.append(''.join(listOfLine)+"\n")
        firstCharOfLine += len(listOfLine)

    toCombineTogether = ''.join(toCombineTogether)
    toCombineTogether = list(toCombineTogether)
    toCombineTogether.pop(len(toCombineTogether)-1)
    toCombineTogether = ''.join(toCombineTogether)
    
    return toCombineTogether, amtOfEmptySpaces

def changePlaceOfCharInArrs(char1toChange: int, char2toChange: int, strOfChar: list[str], xOfChars: list[list[int]], yOfChars: list[list[int]], allClocks: list[int], SpeedsOfChars: list[int], lastButtonUsed: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]]):
    '''
    changePlaceOfCharInArrs(int, int, list[str], list[list[int]], list[list[int]], list[int], list[int], list[str], list[list[int]])

    variables changed:
    amtOfEmptySpacesAtEveryLineOfCharacter
    strOfChar
    xOfChars
    yOfChars
    allClocks
    SpeedsOfChars
    lastButtonUsed

    switches all the data in 2 points in the storage arrays.
    '''
    amtOfEmptySpacesAtEveryLineOfCharacter[char1toChange], amtOfEmptySpacesAtEveryLineOfCharacter[char2toChange] = amtOfEmptySpacesAtEveryLineOfCharacter[char2toChange], amtOfEmptySpacesAtEveryLineOfCharacter[char1toChange]
    strOfChar[char1toChange], strOfChar[char2toChange] = strOfChar[char2toChange], strOfChar[char1toChange]
    xOfChars[char1toChange], xOfChars[char2toChange] = xOfChars[char2toChange], xOfChars[char1toChange]
    yOfChars[char1toChange], yOfChars[char2toChange] = yOfChars[char2toChange], yOfChars[char1toChange]
    allClocks[char1toChange], allClocks[char2toChange] = allClocks[char2toChange], allClocks[char1toChange]
    SpeedsOfChars[char1toChange], SpeedsOfChars[char2toChange] = SpeedsOfChars[char2toChange], SpeedsOfChars[char1toChange]
    lastButtonUsed[char1toChange], lastButtonUsed[char2toChange] = lastButtonUsed[char2toChange], lastButtonUsed[char1toChange]

def unloadCharacter(pointOfCharInArrs: int, strOfChar: list[str], xOfChars: list[list[int]], yOfChars: list[list[int]], allClocks: list[int], SpeedsOfChars: list[int], lastButtonUsed: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]]):
    '''
    unloadCharacter(int, list[str], list[list[int]], list[list[int]], list[int], list[int], list[str], list[list[int]])

    variables changed:
    amtOfEmptySpacesAtEveryLineOfCharacter
    strOfChar
    xOfChars
    yOfChars
    allClocks
    SpeedsOfChars
    lastButtonUsed

    takes out all of the character's properties from all the storage arrays, if you want something to dissapear use this functions.
    '''
    amtOfEmptySpacesAtEveryLineOfCharacter[pointOfCharInArrs] = -1
    strOfChar[pointOfCharInArrs] = -1
    xOfChars[pointOfCharInArrs] = -1
    yOfChars[pointOfCharInArrs] = -1
    allClocks[pointOfCharInArrs] = -1
    SpeedsOfChars[pointOfCharInArrs] = -1
    lastButtonUsed[pointOfCharInArrs] = -1

def replaceCharacter(sprite: str, speed_of_character: int, startingPointOfX: int, startingPointOfY: int, universalClock: int, pointToReplace: int, strOfChar: list[str], xOfChars: list[list[int]], yOfChars: list[list[int]], allClocks: list[int], SpeedsOfChars: list[int], lastButtonUsed: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]]):
    '''
    loadCharacter(str, int, int, int, int, list[str], list[list[int]], list[list[int]], list[int], list[int], list[str], list[list[int]])
    
    variables changed:
    amtOfEmptySpacesAtEveryLineOfCharacter
    strOfChar
    xOfChars
    yOfChars
    allClocks
    SpeedsOfChars
    lastButtonUsed
    
    loads the character and all it's properties such as speed, sprite and more into the screen.
    '''    
    spriteWithoutEmptySpacesAtTheStart, amtOfEmptySpacesPerLine = takeOutEmptySpaces(sprite)
    allCoorsOfCharX, allCoorsOfCharY = moveCharToASpesificPoint(startingPointOfX, startingPointOfY, spriteWithoutEmptySpacesAtTheStart, amtOfEmptySpacesPerLine)

    amtOfEmptySpacesAtEveryLineOfCharacter[pointToReplace] = amtOfEmptySpacesPerLine
    strOfChar[pointToReplace] = spriteWithoutEmptySpacesAtTheStart
    xOfChars[pointToReplace] = allCoorsOfCharX
    yOfChars[pointToReplace] = allCoorsOfCharY
    allClocks[pointToReplace] = universalClock
    SpeedsOfChars[pointToReplace] = speed_of_character
    lastButtonUsed[pointToReplace] = ''

def loadCharacter(sprite: str, speed_of_character: int, startingPointOfX: int, startingPointOfY: int, universalClock: int, strOfChar: list[str], xOfChars: list[list[int]], yOfChars: list[list[int]], allClocks: list[int], SpeedsOfChars: list[int], lastButtonUsed: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]]):
    '''
    loadCharacter(str, int, int, int, int, list[str], list[list[int]], list[list[int]], list[int], list[int], list[str], list[list[int]])
    
    variables changed:
    amtOfEmptySpacesAtEveryLineOfCharacter
    strOfChar
    xOfChars
    yOfChars
    allClocks
    SpeedsOfChars
    lastButtonUsed

    loads the character and all it's properties such as speed, sprite and more into the screen.
    '''    
    spriteWithoutEmptySpacesAtTheStart, amtOfEmptySpacesPerLine = takeOutEmptySpaces(sprite)
    allCoorsOfCharX, allCoorsOfCharY = moveCharToASpesificPoint(startingPointOfX, startingPointOfY, spriteWithoutEmptySpacesAtTheStart, amtOfEmptySpacesPerLine)

    amtOfEmptySpacesAtEveryLineOfCharacter.append(amtOfEmptySpacesPerLine)
    strOfChar.append(spriteWithoutEmptySpacesAtTheStart)
    xOfChars.append(allCoorsOfCharX)
    yOfChars.append(allCoorsOfCharY)
    allClocks.append(universalClock)
    SpeedsOfChars.append(speed_of_character)
    lastButtonUsed.append('')

def outOfBoundsCheckAndReturnToPrevPos(xOfChars: list[list[int]], yOfChars: list[list[int]], borderHeightMax: int, borderHeightMin: int, borderWidthMax: int, borderWidthMin: int, allClocks: list[int], strOfChar: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]], SpeedOfChars) -> list[list[list[int]], list[list[int]]]:
    """
    outOfBoundsCheckAndReturnToPrevPos(list[list[int]], list[list[int]], int, int, int, int, list[int], list[str], list[list[int]]) -> bool
    checks if the last character that moved has hit the borders of the area set by the programmer.
    if they did the function returns true, else, false.
    """
    # the reason we dont take the max value in the array is for when multiple objects have moved in the same tick
    allObjsToCheck = allLatestMovingChars(allClocks)

    for obj in range(len(allObjsToCheck)):
        if strOfChar[allObjsToCheck[obj]] == -1:
            continue
        
        if xOfChars[allObjsToCheck[obj]][0] < borderWidthMin:
            return True
        
        if xOfChars[allObjsToCheck[obj]][len(xOfChars[allObjsToCheck[obj]])-1] > borderWidthMax:
            return True

        if yOfChars[allObjsToCheck[obj]][0] < borderHeightMin:
            return True

        if yOfChars[allObjsToCheck[obj]][len(yOfChars[allObjsToCheck[obj]])-1] > borderHeightMax:
            return True

    return False

def outOfBoundsCheck(xOfChars: list[list[int]], yOfChars: list[list[int]], borderHeightMax: int, borderHeightMin: int, borderWidthMax: int, borderWidthMin: int, allClocks: list[int], strOfChar: list[str], amtOfEmptySpacesAtEveryLineOfCharacter: list[list[int]], SpeedOfChars) -> list[list[list[int]], list[list[int]]]:
    """
    outOfBoundsCheck(list[list[int]], list[list[int]], int, int, int, int, list[int], list[str], list[list[int]]) -> list[list[list[int]], list[list[int]]]
    checks if the last character that moved has hit the borders of the area set by the programmer.
    if they did the function returns them to the place of the border.
    """
    # the reason we dont take the max value in the array is for when multiple objects have moved in the same tick
    allObjsToCheck = allLatestMovingChars(allClocks)

    for obj in range(len(allObjsToCheck)):
        if strOfChar[allObjsToCheck[obj]] == -1:
            continue
        
        if xOfChars[allObjsToCheck[obj]][0] < borderWidthMin:
            xOfChars[allObjsToCheck[obj]], temp = moveCharByItsSpeed(xOfChars[allObjsToCheck[obj]], SpeedOfChars[allObjsToCheck[obj]], 0, plusOrMinus=True)
        
        if xOfChars[allObjsToCheck[obj]][len(xOfChars[allObjsToCheck[obj]])-1] > borderWidthMax:
            xOfChars[allObjsToCheck[obj]], temp = moveCharByItsSpeed(xOfChars[allObjsToCheck[obj]], SpeedOfChars[allObjsToCheck[obj]], 0, plusOrMinus=False)

        if yOfChars[allObjsToCheck[obj]][0] < borderHeightMin:
            yOfChars[allObjsToCheck[obj]], temp = moveCharByItsSpeed(yOfChars[allObjsToCheck[obj]], SpeedOfChars[allObjsToCheck[obj]], 0, plusOrMinus=True)

        if yOfChars[allObjsToCheck[obj]][len(yOfChars[allObjsToCheck[obj]])-1] > borderHeightMax:
            yOfChars[allObjsToCheck[obj]], temp = moveCharByItsSpeed(yOfChars[allObjsToCheck[obj]], SpeedOfChars[allObjsToCheck[obj]], 0, plusOrMinus=False)

    return xOfChars, yOfChars

# TODO: make it
def drawBorders(strToDrawLeftBorder: str, strToDrawRightBorder: str, strToDrawUpBorder: str, strToDrawDownBorder: str, borderWidthMin: int, borderWidthMax: int, borderHeightMin: int, borderHeightMax: int):
    print(term.move_xy(0, 0)+strToDrawLeftBorder*borderHeightMax)
    print(term.move_xy(100, 0)+strToDrawRightBorder*borderHeightMax)
