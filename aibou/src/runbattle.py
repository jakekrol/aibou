#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
from monster import boss
from monster import partner
from aibou.ui.battlescreen import battlescreen
import partnerturn
import ai
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def battle():
    battlescreen.render_monsters(partner, boss)
    while boss.hp > 0 and partner.hp > 0:
        #battlescreen = screen.BattleScreen()
        battlescreen.render_healthbar(partner, boss)
        partnerturn.partner_turn()
        ai.simulate_turn(attacker=boss, defender=partner)
        if partner.hp <= 0 or boss.hp <= 0:
            break

    if boss.hp <= 0:
        battlescreen.victory(partner, boss)
    elif partner.hp <= 0:
        battlescreen.defeat(partner, boss)
    else:
        raise ValueError('Error: battle ended with neither monster losing '\
                'their full hp.')

