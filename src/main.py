import monster
import screen

monster.create_partner('babybee')
monster.create_boss('centipede')
from monster import partner
from monster import boss
screen.make_battlescreen()
screen.make_qtescreen()
from screen import battlescreen
from screen import qtescreen

import battle
battle.battle()
