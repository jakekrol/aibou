#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external
import pathlib
import yaml
import os
import ai
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
import battlemechanics
import monster
import aibou.ui.screen
from aibou.ui.battlescreen import battlescreen
from aibou.ui.qtescreen import qtescreen
from monster import partner
from monster import boss
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
monster_data_path = pathlib.Path(__file__).parent.parent.joinpath('data', 'monsters.yaml')
move_data_path = pathlib.Path(__file__).parent.parent.joinpath('data', 'moves.yaml')

def deal_damage(monster, power, num_events, num_successes):
    monster.hp = monster.hp - (power * (num_events / num_successes))

def calc_evade_result(base_evasion_stat, num_successes, num_events):
   return base_evasion_stat * (num_successes / num_events)

def resolve_move(selection, type, num_successes):
    with move_data_path.open('r') as file:
        move_data = yaml.safe_load(file)
        move_type = move_data[selection]['type'] 
        power = move_data[selection]['power'] 
        num_events = move_data[selection]['num_events'] 
        if 'damage' in move_type:
            deal_damage(boss, power, num_events, num_successes)
        elif 'evade' in move_type:
            efficacy = move_data[selection]['efficacy']
            calc_evade_result(efficacy, num_successes, num_events)
        elif 'status' in move_type:
            pass
        elif len(move_type == 0):
            raise ValueError(f'The move, {selection}\'s type list is empty.')
    return

def partner_turn():
    battlescreen.render_healthbar(partner, boss)
    move = battlescreen.prompt_move(partner)
    with move_data_path.open('r') as file:
        data = yaml.safe_load(file)
        move_type = data[move]['type'] 
        num_events = data[move]['num_events'] 
        event_time = data[move]['event_time'] 

    battlescreen.show_move_usage(partner, move)
    num_successes = qtescreen.start(num_events, event_time)
    battlemechanics.resolve_move(partner, boss, move, num_successes)
    battlescreen.render_healthbar(partner, boss)
