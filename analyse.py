from collections import defaultdict
from pdb import pm

zero = lambda :0

class User:
    def __init__(self, nick):
        self.nick = nick
        self.mentions = defaultdict(zero)
        
    def add_mention(self, mention):
        self.mentions[mention] += 1
    
    def __str__(self):
        return self.nick
    
    def __repr__(self):
        return "<" + self.nick + ">: " + repr(sorted(self.mentions.items(), key = lambda x:-x[1]))


class Analyse:
    def __init__(self, f):
        self.f = f
        self.nicks = {}
        self.users = []
    
    def collect_nicks(self):
        parsed_lines = []
        for line in self.f:
            # 19:21 < dx> edef: hi i'm inside you
            if line[6] == "<":
                nick, line = line[6:].split(">", 1)
                self.nicks[nick] = User(nick)
                self.users.append(nicks[nick])
                parsed_lines.append((nick, line))
            if " is now known as " in line:
                # 07:20 -!- puck1pedia is now known as puckipedia
                old, new = line[10:][:-1].split(" is now known as ") 
                if new in nicks:
                    user = self.nicks[old]
                    user.nick = new
                    self.nicks[new] = user
            return parsed_lines
    
    def collect_mentions(self, parsed_lines):
        for nick, line in parsed_lines:
            for mention in self.nicks.keys():
                if mention in line:
                    self.nicks[nick].add_mention(nicks[mention])

    
    def scale_mentions(self):
        for user in self.users:
            total = sum(user.mentions.values())
            for mention,value in user.mentions.items():
                user.mentions[mention] = round(value * 100.0 / total, 2)

        
    def main(self):
        self.collect_mentions(self.collect_nicks())
        self.scale_mentions()

with open("../logs") as f:
    a = Analyse(f.readlines())
    a.main()




        


