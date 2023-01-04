import monster
import screen
import yaml
import os

def deal_damage(monster, damage):
    monster.hp = monster.hp - damage

def partner_turn(battlescreen, partner, boss):
    move = battlescreen.prompt_move(partner)
    qtescreen = screen.QTE()
    with open(f'{os.getcwd()}/../data/attacks.yaml', 'r') as file:
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

def boss_turn(battlescreen, partner, boss):


def start_turn(battlescreen, partner, boss):
    partner_turn(battlescreen, partner, boss)

def battle(partner, boss):
    while boss.hp > 0 and partner.hp > 0:
        battlescreen = screen.Battle()
        battlescreen.render_monsters(partner, boss)
        battlescreen.render_healthbar(partner, boss)
        start_turn(battlescreen, partner, boss)

    if boss.hp <= 0:
        print(f'{boss.name} has been defeated!')
    elif partner.hp <= 0:
        print(f'{boss.name} has been defeated!')
    else:
        raise ValueError('Error: battle ended with neither monster losing '\
                'their full hp.')


