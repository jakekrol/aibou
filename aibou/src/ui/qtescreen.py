#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external packages
import keyboard # module requires root privleges; check bash_aliases for ex on testing
from rich.align import Align
from rich.layout import Layout
from rich.layout import Panel
from rich.padding import Padding
from rich import print
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# std
import random
from time import sleep
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local modules
from .screen import Screen
from ..battle import qte
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

class QTEScreen(Screen):
    
    def __init__(self):
        Screen.__init__(self)

        self.layout.split_column(
                Layout(name='eventspace'),
                Layout(name='lower')
                )
        self.layout['lower'].size = 4

    def start(self, num_events, event_time):
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

def make_qtescreen():
    global qtescreen
    qtescreen = QTEScreen()

