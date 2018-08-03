from collections import defaultdict
from pdb import pm

class User:
    def __init__(self, nick):
        self.nick = nick
        self.mentions = defaultdict(lambda :0)
        
    def add_mention(self, mention):
        self.mentions[mention] += 1
    
    def __str__(self):
        return self.nick
    
    def __repr__(self):
        return "<" + self.nick + ">"


def extract_nick(line):
    # 19:21 < dx> edef: hi i'm inside you
    if line[6] == "<":
        return line.split("<")[1][1:].split(">")[0]
    else:
        return False


with open("../logs") as f:
    lines = f.readlines()

nicks = {}
users = []

for line in lines[::-1]:
    # going backwords so a user's main nick is the most recent one
    nick = extract_nick(line)
    if nick and nick not in  nicks:
        nicks[nick] = User(nick)
        users.append(nicks[nick])
    if " is now known as " in line:
        # 07:20 -!- puck1pedia is now known as puckipedia
        old, new = line[10:][:-1].split(" is now known as ") 
        # new = more recent
        if new in nicks:
            # if they haven't said anything since changing their name
            nicks[old] = nicks[new]


for line in lines:
    nick = extract_nick(line)
    if nick:
        for mention in nicks.keys():
            if mention in line.split("> ")[1]:
                nicks[nick].add_mention(nicks[mention])

for user in users:
    total = sum(user.mentions.values())
    for mention,value in user.mentions.items():
        user.mentions[mention] = round(value * 100.0 / total, 2)
        user.mentions_so
        


