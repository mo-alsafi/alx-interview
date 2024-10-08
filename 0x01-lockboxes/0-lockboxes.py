#!/usr/bin/python3
"""
    You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
    Write a method that determines if all the boxes can be opened.

    Prototype: def canUnlockAll(boxes)
    boxes is a list of lists
    A key with the same number as a box opens that box
    You can assume all keys will be positive integers
    There can be keys that do not have boxes
    The first box boxes[0] is unlocked
    Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """
        Pseudocode:
        0- see number of boxes
        1- create list to all resierved keys from boxes
        2- since we have the first box (box 0) unlocked retrieve the keys that have it into list of keys and increase in value represent keys we found
            if keys for boxes we can't found and key already in the list ignore it
        3- we have a basic list of keys from box one loop through it and access the boxes crosspondeing to it keys and add it to the list matching the first conditions plus if we found key to box 0 ignore it cause we already have it
        4- the number of boxes it well be bigger than keys we found by one if the boxes have keys to it all (true) cause the the key to box 0 from the start we have we don't retrieve it from box so we increase the keys we found by 1
        5- if the keys we found equals number of boxes return true else false
    """

    keys = []
    numOfBoxes = len(boxes) #equal 7
    foundedKeys = 0
    index = 0 #iterator of list of resierved keys

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for key in boxes[0]: #retrieve the keys on box0 since its open
        if(key < numOfBoxes and key not in keys): #if the key is for box we dont have in boxes list we cant open it so dont add it(like key to box 100 and we only have 7 boxes(indexes)), and dont add duplicate keys
            keys.append(key)
            foundedKeys += 1

    #print(len(keys))  --> to see the keys of box0 which already unlocked
    while(index < len(keys)): #for now the loop well run for number of keys founded in box0 if we unlock other boxes we well put them here so the length well increase and loop well till we unlock all possible boxess
        theKey = keys[index] #keys[index] is one key of list of keys it well go to next key after index increase
        for key in boxes[theKey]: #boxes[theKey] we access a box (list) by it given key (index) and with for key in that box we want to access the key inside that box with out it we get the list
            #print(key)  --> to see what key we dealing with
            if(key < numOfBoxes and key not in keys and key > 0): #since the box0 is already opend no need to store the key if we found one
                keys.append(key)
                foundedKeys += 1
        index += 1

    #print(keys, foundedKeys, numOfBoxes-1)
    if(foundedKeys +1 == numOfBoxes):
        return True
    else:
        return False
    