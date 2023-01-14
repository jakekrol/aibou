#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local modules
import monster
from aibou.ui import battlescreen
from aibou.ui import qtescreen
from aibou.ui import welcomescreen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
monster.create_partner('babybee')
monster.create_boss('centipede')
from monster import partner
from monster import boss
battlescreen.make_battlescreen()
qtescreen.make_qtescreen()
from aibou.ui.battlescreen import battlescreen # load battlescreen instance into namespace
from aibou.ui.qtescreen import qtescreen

import battle
battle.battle()
