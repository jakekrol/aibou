#===============================================================================
# aibou wrapper script
#===============================================================================
# order of imports is important
# game data handlers
def play():
    from .battle import getdata
    getdata.load_monster_data()
    getdata.load_move_data()
    from .ui import battlescreen
    from .ui import qtescreen
    from .ui import homescreen
    battlescreen.make_battlescreen()
    qtescreen.make_qtescreen()
#===============================================================================
    from .battle import monster
    monster.create_partner('babybee')
    monster.create_boss('centipede')
    homescreen.start()
    from .battle import runbattle
#===============================================================================
# homescreen
# show home screen
#===============================================================================
# quickplay
# create monsters
# load monsters into namespace
#from monster import partner
#from monster import boss

# make battlescreens

# start battle
    runbattle.battle()
