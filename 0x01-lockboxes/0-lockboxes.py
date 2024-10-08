#!/usr/bin/python3
"""You have n number of locked boxes in front of you.

    Each box is numbered sequentially from.

    0 to n - 1 and each box may contain keys to the other boxes.
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
    """Pseudocode:.

        0- see number of boxes
        1- create list to all resierved keys from boxes
        2- since we have the first box (box 0) unlocked retrieve
        the keys that
        have it into list of keys and increase in value represent
        keys we found
        if keys for boxes we can't found and key already in the
        list ignore it
        3- we have a basic list of keys from box one loop through
        it and access the
        boxes crosspondeing to it keys and add it to the list
        matching the first 
        conditions plus if we found key to box 0 ignore it cause
        we already have it
        4- the number of boxes it well be bigger than keys we
        found by one if the boxes 
        have keys to it all (true) cause the the key to box 0
        from the start we have we
        don't retrieve it from box so we increase the keys we
        found by 1
        5- if the keys we found equals number of boxes return
        true else false
    """
    keys = []
    num_0f_boxes = len(boxes)
    founded_keys = 0
    index = 0

    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for key in boxes[0]:
        if(key < num_0f_boxes and key not in keys):
            keys.append(key)
            founded_keys += 1

    while(index < len(keys)):
        the_key = keys[index]
        for key in boxes[the_key]:
            if(key < num_0f_boxes and key not in keys and key > 0):
                keys.append(key)
                founded_keys += 1
        index += 1

    if(founded_keys+1 == num_0f_boxes):
        return True
    else:
        return False
