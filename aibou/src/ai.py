#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external 
import random
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local 
import battlemechanics
import monster
from aibou.ui import screen
from aibou.ui.battlescreen import battlescreen # load battlescreen instance into namespace
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def get_move_data(attacker):
    return attacker.moveset.dict

def initialize_weight_dict():
    global weight_dict 
    weight_dict = dict()

def update_weight_dict(attacker, skill_dict_with_move_lists, distribute_weight='select'):
    ''' Update weight_dict based on move skill '''
    total_moves_in_skill_dict = 0 # initialize counter
    for move_list in skill_dict_with_move_lists.values():
        total_moves_in_skill_dict += len(move_list)
    if total_moves_in_skill_dict == 0:
        return 
    for skill, move_list in skill_dict_with_move_lists.items():
        for move in move_list:
            if skill == 'easy':
                weight_dict[move] += 0.25
            elif skill == 'medium':
                weight_dict[move] += 0.2
            elif skill == 'hard':
                weight_dict[move] += 0.15
            else:
                pass
    sum_weights = sum(weight_dict.values())
    remainder = 1 - sum_weights
    remainder_portion = remainder / total_moves_in_skill_dict
    if distribute_weight == 'select':
        # distribute leftover weights to select moves 
        for move,weight in weight_dict.items():
            for skill,move_list in skill_dict_with_move_lists.items():
                if move in move_list:
                    weight_dict[move] += remainder_portion
    elif distribute_weight == 'all':
        # distribute to all moves
        move_data = get_move_data(attacker)
        for move, data in move_data.items():
            weight_dict[move] += remainder_portion
    print('weight dict: ', weight_dict)
    return

def is_weight_dict_full():
    if sum(weight_dict.values()) > 0.98 and sum(weight_dict.values()) < 1.02:
        print('sum of weight_dict.values', sum(weight_dict.values()), weight_dict)
        print('weight dict is full')
        return True
    else:
        return False

def check_kill(attacker, defending_monster):
    ''' Adds weight to moves that can kill defending_monster '''
    move_data = get_move_data(attacker)
    final_blows = {'easy': [], 'medium': [], 'hard': []}
    for move,data in move_data.items():
        weight_dict[move] = 0.0
        if move_data[move]['power'] >= defending_monster.hp:
            skill = data['skill']
            final_blows[skill].append(move)
    update_weight_dict(attacker, final_blows, distribute_weight='select')

def check_heal(attacker):
    ''' Boss attempts to heal or dodge when below 50% hp '''
    if is_weight_dict_full() == True:
        return
    if attacker.hp >= 0.5 * attacker.max_hp:
        print('check_heal() is running')
        return
    else: # add weights to healing and dodging moves
        move_data = get_move_data(attacker)
        heal_and_evade_moves = {'easy': [], 'medium': [], 'hard': []}
        for move,data in move_data.items():
            # check if there's a healing move
            try: # lifesteal_portion is not always specified in move config
                if data['lifesteal_portion']:
                    heal_and_evade_moves[data['skill']].append(move)
            except KeyError:
               pass 
            if data['type'] == 'evade':
                heal_and_evade_moves[data['skill']].append(move)

        update_weight_dict(
                attacker,
                heal_and_evade_moves,
                distribute_weight='all'
                )
        return

def finalize_weight_dict(attacker):
    ''' 
    Finalizes weight_dict by checking if weights add to 1. In the case of
    a detected kill or detected heal, then the weights should already be 1.
    If not, then this function will distribute the weights uniformly to each move.
    '''
    # if weights are not already one, distribute them uniformly
    if is_weight_dict_full() == False:
        moveset_dict = get_move_data(attacker)
        total_moves = len(moveset_dict.keys())
        for move in moveset_dict.keys():
            weight_dict[move] += (1 / total_moves)
        print('finalizing weight_dict', weight_dict)
    # final check for weights
    if is_weight_dict_full() == False:
        raise ValueError('ai move weights do not add to one', weight_dict)
    return

def choose_weighted_moves():
    options = []
    weights = []
    for move, weight in weight_dict.items():
        options.append(move)
        weights.append(weight) 
    selection = random.choices(options, weights=weights, k=1)[0]
    return selection

def simulate_qte(selected_move, attacker):
    moveset_dict = get_move_data(attacker)
    move_data = moveset_dict[selected_move]
    max_damage = move_data['power']
    skill = move_data['skill']
    num_events = move_data['num_events']
    if skill == 'easy':
        p_success = 0.9
    elif skill == 'medium':
        p_success = 0.8
    elif skill == 'hard':
        p_success = 0.7
    else:
        raise ValueError('skill must be easy, medium, or hard')
    p_fail = 1 - p_success
    weights = [p_fail, p_success]
    success_count = 0
    for event in range(num_events):
        outcome = random.choices([0,1], weights=weights, k=1)[0] # get item from single element list
        success_count += outcome
    return success_count

def check_lifesteal(attacker, selected_move):
    move_data = get_move_data(attacker)
    try:
        lifesteal_portion = move_data[selected_move]['lifesteal_portion']
        return lifesteal_portion
    except KeyError:
        return None

def simulate_turn(attacker, defender):
    initialize_weight_dict()
    check_kill(attacker, defender)
    check_heal(attacker)
    finalize_weight_dict(attacker)
    selection = choose_weighted_moves()
    print(weight_dict)
    battlescreen.show_move_usage(attacker, selection)
    success_count = simulate_qte(
            selection, attacker
            )
    battlemechanics.resolve_move(attacker, defender, selection, success_count)
    battlescreen.render_healthbar(partner=defender, boss=attacker)
    return
