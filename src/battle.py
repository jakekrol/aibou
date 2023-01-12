import monster
import screen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
from monster import partner
from monster import boss
from screen import battlescreen
from screen import qtescreen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
import yaml
import os
import ai

def deal_damage(monster, damage):
    monster.hp = monster.hp - damage

def partner_turn():
    move = battlescreen.prompt_move(partner)
    qtescreen = screen.QTEScreen()
    with open(f'{os.getcwd()}/../data/moves.yaml', 'r') as file:
        data = yaml.safe_load(file)
        power = data[move]['power'] 
        skill = data[move]['skill'] 
        num_events = data[move]['num_events'] 
        event_time = data[move]['event_time'] 

    num_successes = qtescreen.start(power, num_events, event_time)
    if num_successes > 0:
        damage = power * (num_events/num_successes)
    else:
        damage = 0
    deal_damage(boss, damage)
    battlescreen.render_healthbar(partner, boss)

def start_turn():
    partner_turn()
    ai.simulate_turn(attacking_monster=boss, defending_monster=partner)

def battle():
    battlescreen.render_monsters(partner, boss)
    while boss.hp > 0 and partner.hp > 0:
        #battlescreen = screen.BattleScreen()
        battlescreen.render_healthbar(partner, boss)
        start_turn()
        if partner.hp <= 0 or boss.hp <= 0:
            break

    if boss.hp <= 0:
        battlescreen.victory(partner, boss)
    elif partner.hp <= 0:
        battlescreen.defeat(partner, boss)
    else:
        raise ValueError('Error: battle ended with neither monster losing '\
                'their full hp.')


