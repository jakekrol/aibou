from color import red, blue, green, yellow
import os
#from pathlib import Path
import yaml

class Monster():

    _instances = []

    def __init__(self, name):
        self.name = name
        self.art_file = name + '.txt'
        self.alive = True
        # get art 
        with open(f'{os.getcwd()}/../art/{self.art_file}', 'r') as file:
            lines = []
            for line in file:
                lines.append(line)
            self.text = ''.join(lines)
        self.height = self.text.count('\n')

        # get monster data
        with open(f'{os.getcwd()}/../data/monsters.yaml', 'r') as file:
           data = yaml.safe_load(file)
           self.data = data[name]
        self.hp = self.data['hp']
        self.movelist = self.data['movelist']

        #self.name = Path(art_file).stem
        self._instances.append(self)

    def display(self):
        print(self.text)

    def color(self, choice):
        if choice in ['red', 'blue', 'green', 'yellow']:
            self.text = choice(self.text)

    def check_health(self):
        if self.hp > 0:
            pass
        else:
            self.alive = False
    
    def update_hp(self, delta):
        self.hp = self.hp - delta
        check_health()


class Partner(Monster):

    def __init__(self, name):
        Monster.__init__(self, name)
        self.type = 'partner'


class Boss(Monster):

    def __init__(self, name):
        Monster.__init__(self, name)
        self.type = 'boss'

#def load_art(art_file):
#    with open(f'{os.getcwd()}/../art/{art_file}', 'r') as file:
#        lines = []
#        for line in file:
#            lines.append(line)
#        formatted_art = ''.join(lines)
#        return formatted_art


