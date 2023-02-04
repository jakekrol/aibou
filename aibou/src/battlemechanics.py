#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external
import os
import random
import yaml
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
import ai
import monster
from aibou.ui.battlescreen import battlescreen
from getdata import monster_data, move_data
from monster import partner
from monster import boss
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
def deal_damage(monster, power, num_events, num_successes):
    damage = power * (num_successes / num_events)
    monster.hp = monster.hp - damage
    return damage

def resolve_heal(monster, power, num_events, num_successes):
    heal_amount = power * (num_successes / num_events)
    if (monster.hp + heal_amount) > monster.max_hp:
        # recalculate heal amount to be 
        heal_amount = monster.max_hp - monster.hp
    monster.hp += heal_amount
    return heal_amount

def resolve_lifesteal(attacker, selected_move, damage):
    lifesteal_portion = move_data[selected_move]['lifesteal_portion']
    attacker.hp += lifesteal_portion * damage
    # prevent overhealing
    if attacker.hp > attacker.max_hp:
        attacker.hp = attacker.max_hp
    return lifesteal_portion

def calc_evade_result(monster, base_evasion_stat, num_successes, num_events):
    evasion_success_chance = base_evasion_stat * (num_successes / num_events)
    weights = [evasion_success_chance, 1 - evasion_success_chance]
    result = random.choices(['success', 'fail'], weights, k=1)[0]
    return result

def resolve_evade(defender):
    efficacy = defender.status['evading']['efficacy']
    result = random.choices(['success', 'fail'], [efficacy, 1 - efficacy], k=1)[0]
    defender.status['evading']['duration'] -= 1
    duration = defender.status['evading']['duration']
    if defender.status['evading']['duration'] == 0:
    # remove evading status with dictionary comprehension filter
        defender.status = \
                {status:info for (status,info) in defender.status.items() if status != 'evading'}

    return result, duration

def resolve_move(attacker, defender, selection, num_successes):
    move_type = move_data[selection]['type'] 
    power = move_data[selection]['power'] 
    num_events = move_data[selection]['num_events'] 
    # apply move and print outcome to screen
    if 'damage' in move_type:
        if 'evading' in defender.status.keys():
            result, duration = resolve_evade(defender)
            battlescreen.show_evade_outcome(attacker, defender, selection, result, duration)
            if result == 'success':
                return 
        damage = deal_damage(defender, power, num_events, num_successes)
        outcome_text = f'{attacker.name} dealt {damage} damage to {defender.name}!'
        target = defender.type
        battlescreen.show_damage(partner, boss, target, damage)
        if 'lifesteal' in move_type:
            lifesteal_portion = resolve_lifesteal(attacker, selection, damage)
            outcome_text = f'{attacker.name} dealt {damage} damage to {defender.name} '\
            f'and healed {lifesteal_portion * power}!'
    elif 'heal' in move_type:
        heal_amount = resolve_heal(attacker, power, num_events, num_successes)
        target = attacker.type
        battlescreen.show_heal(partner, boss, target, heal_amount)
        outcome_text = f'{attacker.name} healed {heal_amount}hp!'
    elif 'status' in move_type:
        if move_data[selection]['effect']['type'] == 'evade':
            efficacy = move_data[selection]['effect']['efficacy']
            duration = move_data[selection]['effect']['duration']
            result = calc_evade_result(attacker, efficacy, num_successes, num_events)
            if result == 'success':
                attacker.status['evading'] = {'efficacy': efficacy, 'duration': duration}
                outcome_text = f'{attacker.name} will attempt to evade the next '\
                        f'{duration} attacks!'
            elif result == 'fail':
                outcome_text = f'{attacker.name}\'s evasion attempt failed!'
    elif len(move_type) == 0:
        raise ValueError(f'The move, {selection}\'s type list is empty.')
    battlescreen.show_move_outcome(
            attacker, defender, selection, num_events, num_successes, outcome_text
            )
    return

