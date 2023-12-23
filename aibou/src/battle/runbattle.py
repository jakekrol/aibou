#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
from .monster import boss
from .monster import partner
from ..ui import battlescreen
from ..ui.battlescreen import battlescreen
from . import partnerturn
from . import ai
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def battle():
    battlescreen.render_monsters(partner, boss)
    while boss.hp > 0 and partner.hp > 0:
        #battlescreen = screen.BattleScreen()
        battlescreen.render_healthbar(partner, boss)
        partnerturn.partner_turn()
        # break if either monster is at or below 0 hp after partner turn
        if partner.hp <= 0 or boss.hp <= 0:
            break
        ai.simulate_turn(attacker=boss, defender=partner)

    if boss.hp <= 0:
        battlescreen.victory(partner, boss)
    elif partner.hp <= 0:
        battlescreen.defeat(partner, boss)
    else:
        raise ValueError('Error: battle ended with neither monster losing '\
                'their full hp.')

