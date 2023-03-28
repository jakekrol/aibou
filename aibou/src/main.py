#===============================================================================
# aibou wrapper script
#===============================================================================
# order of imports is important
#===============================================================================
# game data handlers
import getdata 
getdata.load_monster_data()
getdata.load_move_data()
#===============================================================================
# homescreen
from aibou.ui import battlescreen
from aibou.ui import qtescreen
from aibou.ui import homescreen
# show home screen
homescreen.start()
#===============================================================================
# quickplay
# create monsters
import monster
monster.create_partner('babybee')
monster.create_boss('centipede')
# load monsters into namespace
#from monster import partner
#from monster import boss

# make battlescreens
battlescreen.make_battlescreen()
qtescreen.make_qtescreen()

# start battle
import runbattle
runbattle.battle()

