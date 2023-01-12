from color import red, blue, green, yellow
import os
#from pathlib import Path
import yaml

class Moveset():
    ''' Store move data for a specific monster '''

    def __init__(self, monster_name):
        self.monster_name = monster_name
        with open(f'{os.getcwd()}/../data/monsters.yaml', 'r') as file:
           monster_data = yaml.safe_load(file)
           self.move_names = monster_data[monster_name]['moveset']
        with open(f'{os.getcwd()}/../data/moves.yaml', 'r') as file:
            move_data = yaml.safe_load(file)
            self.dict = dict()
            for move in self.move_names:
                self.dict[move] = move_data[move]

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
        self.max_hp = self.hp
        self.moveset = Moveset(self.name)
        #self.movelist = self.data['movelist']

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

def create_partner(name):
    global partner
    partner = Partner(name)

def create_boss(name):
    global boss
    boss = Boss(name)

