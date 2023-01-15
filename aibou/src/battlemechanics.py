#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external
import os
import pathlib
import random
import yaml
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
import ai
import monster
#import aibou.ui.screen
from aibou.ui.battlescreen import battlescreen
#from aibou.ui.qtescreen import qtescreen
from monster import partner
from monster import boss
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
monster_data_path = pathlib.Path(__file__).parent.parent.joinpath('data', 'monsters.yaml')
move_data_path = pathlib.Path(__file__).parent.parent.joinpath('data', 'moves.yaml')

def deal_damage(monster, power, num_events, num_successes):
    damage = power * (num_successes / num_events)
    monster.hp = monster.hp - damage
    return damage

def resolve_heal(monster, power, num_events, num_successes):
    heal_amount = power * (num_successes / num_events)
    if (monster.hp + heal_amount) > monster.max_hp:
        # recalculate heal amount to be 
        heal_amount = monster.max_hp - monster.hp
        monster.hp = monster.max_hp
    monster.hp += heal_amount
    return heal_amount

def resolve_lifesteal(attacker, selected_move):
    lifesteal_portion = move_data[selected_move]['lifesteal_portion']
    attacker.hp += lifesteal_portion
    # prevent overhealing
    if attacker.hp > attacker.max_hp:
        attacker.hp = attacker.max_hp
    return lifesteal_portion

def calc_evade_result(monster, base_evasion_stat, num_successes, num_events):
   evasion_success_chance = base_evasion_stat * (num_successes / num_events)
   weights = [evasion_success_chance, 1 - evasion_success_chance]
   result = random.choices(['success', 'fail'], weights, k=1)
   if result == 'success':
       monster.status.append('evading')
   return result

def resolve_status():
    monsters = [partner, boss]
    for monster in monsters:
        if monster.status:
            if 'evading' in monster.status:
                pass

def resolve_move(attacker, defender, selection, num_successes):
    with move_data_path.open('r') as file:
        global move_data
        move_data = yaml.safe_load(file)
        move_type = move_data[selection]['type'] 
        power = move_data[selection]['power'] 
        num_events = move_data[selection]['num_events'] 
        # apply move and print outcome to screen
        if 'damage' in move_type:
            damage = deal_damage(defender, power, num_events, num_successes)
            outcome_text = f'{attacker.name} dealt {damage} damage to {defender.name}!'
            target = defender.type
            battlescreen.show_damage(partner, boss, target, damage)
            if 'lifesteal' in move_type:
                lifesteal_portion = resolve_lifesteal(attacker, selection)
                outcome_text = f'{attacker.name} dealt damage{damage} damage to {defender.name} '\
                f'and healed {lifesteal_portion}!'
        elif 'evade' in move_type:
            efficacy = move_data[selection]['efficacy']
            result = calc_evade_result(efficacy, num_successes, num_events)
            outcome_text = f'The result of {attacker.name}\'s evade is a {result}'
        elif 'heal' in move_type:
            heal_amount = resolve_heal(attacker, power, num_events, num_successes)
            target = attacker.type
            battlescreen.show_heal(partner, boss, target, heal_amount)
            outcome_text = f'{attacker.name} healed {heal_amount}hp!'
        elif 'status' in move_type:
            defending_monster.status.append(move_data['effect']['type'])
            pass
        elif len(move_type) == 0:
            raise ValueError(f'The move, {selection}\'s type list is empty.')
        battlescreen.show_move_outcome(
                attacker, defender, selection, num_events, num_successes, outcome_text
                )
        return

