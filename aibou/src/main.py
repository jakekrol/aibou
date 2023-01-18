#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# order of imports is important
import getdata 
getdata.load_monster_data()
getdata.load_move_data()
from getdata import monster_data, move_data

from aibou.ui import battlescreen
from aibou.ui import qtescreen
from aibou.ui import welcomescreen
# show welcome screen
welcomescreen.show_title()
# create monsters
import monster
monster.create_partner('babybee')
monster.create_boss('centipede')
# load monsters into namespace
from monster import partner
from monster import boss
# make battlescreens
battlescreen.make_battlescreen()
qtescreen.make_qtescreen()
from aibou.ui.battlescreen import battlescreen # load battlescreen instance into namespace
from aibou.ui.qtescreen import qtescreen

# start battle
import runbattle
runbattle.battle()
