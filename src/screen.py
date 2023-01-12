#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external packages
from rich import print
from rich.layout import Layout
from rich.layout import Panel
from rich.padding import Padding
from rich.prompt import Prompt
from rich.align import Align
from rich.columns import Columns
from rich.text import Text
#from rich.style import Style
#from rich.console import Console
from time import sleep
import keyboard # module requires root privleges; check bash_aliases for ex on testing
import random
import sys
import termios
from termios import tcflush, TCIFLUSH
# ============================================================================== 
# local modules
import monster
import qte
from qte import Event
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
class Screen():

    def __init__(self):
        self.layout = Layout()

    def show(self):
        print(self.layout)

class Menu(Screen):
    pass

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
        # prevent negative hp on death
        if monster.hp <= 0:
            hp_text = '0'
        else:
            hp_text = str(monster.hp)
        nametext = Text(monster.name + ': ')
        nametext.stylize('italic ' + self.namecolor + ' on white')
        hearttext = Text(('\u2665' * num_hearts) + ('X' * num_Xs) + ' ' + hp_text)
        hearttext.stylize('red on white')
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

    def unrender_monster(self, monster):

        if monster.type == 'partner':
            columns = Columns([' ', self.boss_render], expand=True)
        elif monster.type == 'boss':
            columns = Columns([self.partner_render], ' ', expand=True)
        else:
            raise ValueError('wrong value for Monster.type')
        self.layout['middle'].update(Panel(columns))

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
        sleep(1.5)


    def prompt_move(self, monster):
        tcflush(sys.stdin, TCIFLUSH)# clear stdin queue to prevent entering old key presses
        move_data = monster.moveset.dict
        choices = dict()
        prompts = list()
        for index,move in enumerate(monster.moveset.move_names):
            prompts.append(f'{index + 1}->{move}')
            choices[str(index + 1)] = move
        prompts = '\t\t'.join(prompts)
        self.layout['lower'].update(Panel(f"Choose an attack:\n{prompts}"))
        self.show()
        def show_move_data(key):
            print(f'\n{choices[key]}: {move_data[choices[key]]}')
            tcflush(sys.stdin, TCIFLUSH)
        for key in choices.keys():
            keyboard.add_hotkey(
                    f'i+{key}', show_move_data, args=[key]
                    )
        selection = Prompt.ask(choices=choices.keys())
                                
        if selection in choices:
            for key in choices.keys():
                keyboard.remove_hotkey(f'i+{key}')
            self.show_move_usage(monster, choices[selection])
        else:
            self.prompt_move(monster)
        return choices[selection]

    def show_qte_outcome(self, monster, move, num_events, num_successes, damage, lifesteal=None):
        if lifesteal == None:
            message = f'{monster.name} passed {num_successes}/{num_events} skill '\
                    f'checks and deals {damage} damage!'
        else:
            message = f'{monster.name} passed {num_successes}/{num_events} skill '\
                    f'checks and deals {damage} damage and heals {lifesteal} hp!'

        self.layout['lower'].update(Panel(message))
        self.show()
        sleep(2)

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

class QTEScreen(Screen):
    
    def __init__(self):
        Screen.__init__(self)

        self.layout.split_column(
                Layout(name='eventspace'),
                Layout(name='lower')
                )
        self.layout['lower'].size = 4

    def start(self, power, num_events, event_time):
        ''' Setup qte display and call qte functions for updates '''
        result_tally = 0
        for i in range(num_events):
# ============================================================================== 
            self.layout['lower'].update(Panel('Press the key!'))
            sleep(1.5) # delay before event starts
            character = qte.randomcharacter()
            # display char
            self.layout['eventspace'].update(
                    Panel(
                        Align(
                            Padding(character, (1,1), style = 'on blue'),
                            align=random.choice(['left', 'center', 'right']),
                            vertical=random.choice(['top', 'middle', 'bottom'])
                            )
                        )
                    )
            self.show()

            result, feedback = qte.runevent(character, event_time)
            if result == 0:
                self.layout['eventspace'].update(
                        Panel(
                            Align(
                                Padding(feedback, (1,1), style = 'on red'),
                                align='center',
                                vertical='middle')
                            )
                        )
                self.layout['lower'].update(
                        Panel(
                            Align(
                                Padding('Fail', style = 'on red'),
                                align='center',
                                vertical='middle')
                            )
                        )
            elif result == 1:
                self.layout['eventspace'].update(
                        Panel(
                            Align(
                                Padding(feedback, (1,1), style = 'on green'),
                                align='center',
                                vertical='middle')
                            )
                        )
                self.layout['lower'].update(
                        Panel(
                            Align(
                                Padding('Success!', style = 'on green'),
                                align='center',
                                vertical='middle')
                            )
                        )
                result_tally += 1
            else:
                raise ValueError(
                        'Unexpected value for <result>',
                        result
                        )
            # display result
            self.show()
# ============================================================================== 
        sleep(1.5) # pause and show final feedback before moving to damage step
        self.show()
        return result_tally

def make_battlescreen():
    global battlescreen
    battlescreen = BattleScreen() 

def make_qtescreen():
    global qtescreen
    qtescreen = QTEScreen()
