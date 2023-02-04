#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external packages
from rich import print
from rich.layout import Layout
from rich.layout import Panel
from rich.prompt import Prompt
from rich.align import Align
from rich.columns import Columns
from rich.text import Text
from time import sleep
import keyboard 
import sys
import termios
from termios import tcflush, TCIFLUSH
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local modules
from aibou.src import monster
from aibou.ui import screen
from aibou.ui.screen import Screen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class Healthbar():
    
    def __init__(self, monster):
        max_hearts = int(monster.max_hp // 15)
        num_hearts = int(monster.hp // 15) # rounds down
        num_Xs = max_hearts - num_hearts 

        if monster.type == 'partner':
            self.namecolor = 'green'
        elif monster.type == 'boss':
            self.namecolor = 'red'
        else:
            raise ValueError(
                    'Bad value for monster.type during health bar ' \
                    'initializaiton.\nIs a Monster object being used for ' \
                    'battle instead of a Partner or Boss?'
                    )
        # make final heart stay while monster is alive
        if num_hearts == 0 and monster.hp > 0:
            num_hearts = 1
        # prevent negative hp display on death
        if monster.hp <= 0:
            hp_text = '0'
        else:
            hp_text = str(round(monster.hp, 1))
        nametext = Text(monster.name + ': ')
        nametext.stylize('italic ' + self.namecolor + ' on white')
        hearttext = Text(('\u2665' * num_hearts) + ('X' * num_Xs) + ' ' + hp_text)
        hearttext.stylize('red on white')
        # add status text
        if monster.status.keys():
            if 'evading' in monster.status.keys():
                statustext = Text('E')
                statustext.stylize('italic white on purple')
                # partner status on right of healthbar
                if monster.type == 'partner':
                    self.text = nametext + hearttext + ' ' + statustext
                # boss status on left of health bar
                if monster.type == 'boss':
                    self.text = statustext + ' ' + nametext + hearttext
        else:
            self.text = nametext + hearttext


class BattleScreen(Screen):

    def __init__(self):
        Screen.__init__(self) 

        self.layout.split_column(
                Layout(name='upper'),
                Layout(name='middle'),
                Layout(name='lower')
                )
        self.layout['middle'].ratio = 4
        self.layout['lower'].size = 4
        self.layout['upper'].size = 3

    def fit_monster(self, monster):
        self.layout['middle'].minimum_size = monster.height + 2 # add 2 lines for panel outline

    def render_monsters(self, partner, boss):
        # fit monsters in layout height
        for monster in [partner, boss]:
            self.fit_monster(monster)
        self.partner_render = Align(partner.text, align='left', vertical='bottom')
        self.boss_render = Align(boss.text, align='right', vertical='top')
        columns = Columns([self.partner_render, self.boss_render], expand=True)
        self.layout['middle'].update(Panel(columns))
        return 

    def unrender_monster(self, monster):
        if monster.type == 'partner':
            columns = Columns([' ', self.boss_render], expand=True)
        elif monster.type == 'boss':
            columns = Columns([self.partner_render], ' ', expand=True)
        else:
            raise ValueError('wrong value for Monster.type')
        self.layout['middle'].update(Panel(columns))
        return

    def show_damage(self, partner, boss, target, damage):
        partner_render = Text(partner.text)
        boss_render = Text(boss.text)
        if target == 'partner':
            partner_render.append(f'-{str(damage)}', style='bold red')
        elif target == 'boss':
            boss_render.append(f'-{str(damage)}', style='bold red')
        partner_render = Align(partner_render, align='left', vertical='bottom')
        boss_render = Align(boss_render, align='right', vertical='top')
        columns = Columns([partner_render, boss_render], expand=True)
        self.layout['middle'].update(Panel(columns))
        self.show()
        self.pause(2)
        self.render_monsters(partner, boss)

    def show_heal(self, partner, boss, target, heal_amount):
        partner_render = Text(partner.text)
        boss_render = Text(boss.text)
        if target == 'partner':
            partner_render.append(f'+{str(heal_amount)}', style='bold green')
        elif target == 'boss':
            boss_render.append(f'+{str(heal_amount)}', style='bold green')
        partner_render = Align(partner_render, align='left', vertical='bottom')
        boss_render = Align(boss_render, align='right', vertical='top')
        columns = Columns([partner_render, boss_render], expand=True)
        self.layout['middle'].update(Panel(columns))
        self.show()
        self.pause(2)
        self.render_monsters(partner, boss)

    def render_healthbar(self, partner, boss):
        partner_hp_render = Align(
                Healthbar(partner).text,
                align='left',
                vertical='bottom'
                )
        boss_hp_render = Align(Healthbar(boss).text,
                               align='right',
                               vertical='bottom'
                               )
        columns = Columns([partner_hp_render, boss_hp_render], expand=True)
        self.layout['upper'].update(Panel(columns))
        self.show()

    def show_move_usage(self, attacking_monster, selected_move):
        self.layout['lower'].update(
                Panel(f'{attacking_monster.name} uses {selected_move}')
                )
        self.show()
        self.pause(1.5)

    def prompt_move(self, monster):
        tcflush(sys.stdin, TCIFLUSH)# clear stdin queue to prevent entering old key presses
        move_data = monster.moveset.dict
        # initialize options dict and prompt list
        options = {'0': 'evade'}
        prompts = ['0->evade']
        for index,move in enumerate(monster.moveset.move_names):
            prompts.append(f'{index + 1}->{move}')
            options[str(index + 1)] = move
        prompts = '    '.join(prompts)
        self.layout['lower'].update(Panel(f"Choose an attack:\n{prompts}"))
        self.show()
        def show_move_data(key):
            print(f'\n{options[key]}: {move_data[options[key]]}')
            tcflush(sys.stdin, TCIFLUSH)
        for key in options.keys():
            keyboard.add_hotkey(
                    f'i+{key}', show_move_data, args=[key]
                    )
        selection = Prompt.ask(choices=options.keys())
                                
        if selection in options:
            for key in options.keys():
                keyboard.remove_hotkey(f'i+{key}')
            self.show_move_usage(monster, options[selection])
        else:
            self.prompt_move(monster)
        return options[selection]

    def show_evade_outcome(self, attacker, defender, move, result, duration):
        if result == 'success':
            result_message = f'{defender.name} successfully evaded {attacker.name}\'s '\
                    f'{move}!'
        if result == 'fail':
            result_message = f'{defender.name}\'s evade attempt failed!'
        if duration > 0:
            duration_message = f'{defender.name} will attempt to evade {duration} more '\
                    f'attack(s).'
        if duration == 0:
            duration_message = f'{defender.name} is no longer evading.'
        message = result_message + '\n' + duration_message
        self.layout['lower'].update(Panel(message))
        self.show()
        self.pause(3)

    def show_move_outcome(self, attacker, defender, move, num_events, num_successes, bonus_text):
        message = f'{attacker.name} passed {num_successes}/{num_events} skill '\
                'checks. ' + bonus_text
        self.layout['lower'].update(Panel(message))
        self.show()
        self.pause(3)

    def victory(self, partner, boss):
        self.unrender_monster(boss)
        self.layout['lower'].update(
                Panel(f'{partner.name} defeated {boss.name}!')
        )
        self.show()

    def defeat(self, partner, boss):
        self.unrender_monster(partner)
        self.layout['lower'].update(
                Panel(f'{partner.name} has been defeated.')
        )
        self.show()

def make_battlescreen():
    global battlescreen
    battlescreen = BattleScreen() 
