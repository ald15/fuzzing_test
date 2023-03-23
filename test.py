
#!/usr/bin/env python
# encoding: utf-8
"""
Example Python Module for AFLFuzz

@author:     ald15

"""

import random
import os


FILE_NAME = os.getcwd() + "/data.txt"
COMMANDS = []

def getData():
    with open (FILE_NAME, "r+", encoding="utf8") as f:
        COMMANDS = [i.strip().encode(encoding="utf-8") for i in f.readlines()]
    return COMMANDS

def init(seed):
    random.seed(seed)


def deinit(): pass


def fuzz(buf, add_buf, max_size):
    COMMANDS = getData()
    option = random.randint(0, 2) # option: 0, 1, 2
    #print(f"OPTION={option}")
    #print("Before: ", buf)
    '''
        Option #0:
            add a single data (text) from COMMANDS to the beginning of the input buffer
        Option #1:
            add a single tags from COMMANDS to the beginning of the input buffer
        Option #2:
            add a single tag/data from COMMANDS to the beginning of the input buffer
    '''
    if option == 0:
        curCommands = list(filter(lambda i: i.count(b"<")==0, COMMANDS))
        command = random.choice(curCommands)
        command = command[:command.index(b" ")]
        ret = bytearray(command) + buf
    elif option == 1:
        start, end = "", ""
        command = random.choice(COMMANDS)
        start, end = command[:command.index(b" ")], command[command.index(b" ")+1:]
        #print(start, end)
        ret = bytearray(start) + buf + bytearray(end)
    elif option == 2:
        findTags, tags = [], []
        start, end = b"", b""
        cur, s = [0, 0], 1 # pos of tag's open/close brackets; beggining of the tag
        for i in range(0, len(buf)):
            if (s):
                if (chr(buf[i])=="<"):
                    cur[0] = i
                    start = 0
            else:
                if (chr(buf[i])==">"):
                    cur[1] = i
                    findTags.append(cur)
                    cur, s = [0, 0], 1
        if (len(findTags)>1):
            tags = [findTags[0], findTags[random.randint(1, len(findTags)-1)]]
            start = buf[tags[0][0]:tags[0][1]+1]
            end = buf[tags[1][0]:tags[1][1]+1]
            ret = buf[:tags[0][0]] + end + buf[tags[0][1]+1:tags[1][0]] + start + buf[tags[1][1]+1:]
        else: ret=buf
    #print("After: ", ret)

    return ret
