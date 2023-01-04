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
        num_hearts = int(monster.hp // 20) # rounds down

        if monster.type == 'partner':
            self.namecolor = 'blue'
        elif monster.type == 'boss':
            self.namecolor = 'purple'
        else:
            raise ValueError(
                    'Bad value for monster.type during health bar ' \
                    'initializaiton.\nIs a Monster object being used for ' \
                    'battle instead of a Partner or Boss?'
                    )
        nametext = Text(monster.name + ': ')
        nametext.stylize('italic ' + self.namecolor + ' on white')
        hearttext = Text('\u2665' * num_hearts)
        hearttext.stylize('red on white')
        self.text = nametext + hearttext

class Battle(Screen):

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
        partner_render = Align(partner.text, align='left', vertical='bottom')
        boss_render = Align(boss.text, align='right', vertical='top')
        columns = Columns([partner_render, boss_render], expand=True)
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

#    def add_partner(self, monster):
#        # size screen for monsters
#        pass
#        self.fit_monster(monster)
#        self.layout['middle'].update(
#                Panel(
#                    Align(
#                        monster.text,
#                        align='left',
#                        vertical='bottom'
#                    )
#                )
#        )
#
#    def add_boss(self, monster):
#        # size screen for monsters
#        self.fit_monster(monster)
#        self.layout['rightmiddle'].update(
#                Panel(
#                    Align(
#                    monster.text,
#                    align='right',
#                    vertical='top'
#                    )
#                )
#        )

    def prompt_move(self, monster):
        choices = dict()
        prompts = list()
        for index,move in enumerate(monster.movelist):
            prompts.append(f'{index + 1}->{move}')
            choices[str(index + 1)] = move
        prompts = '\t\t'.join(prompts)
        self.layout['lower'].update(Panel(f"Choose an attack:\n{prompts}"))
        self.show()

        selection = Prompt.ask(choices=choices.keys())
        if selection in choices:
            self.layout['lower'].update(
                    Panel(f'{monster.name} uses {choices[selection]}')
                    )
        else:
            self.prompt_move(monster)
        self.show()
        sleep(1.5)
        return choices[selection] # returns name of move

class QTE(Screen):
    
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



