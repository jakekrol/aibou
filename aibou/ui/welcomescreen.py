#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
from rich.align import Align
from rich.panel import Panel
from rich import print
import pathlib
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
from aibou.ui import screen
from aibou.ui.screen import Screen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
class WelcomeScreen(Screen):

    def __init__(self):
        Screen.__init__(self) 
        self.layout.ratio = 1


    def show(self, icon):
        print(icon)


def make_title():
    title_ascii_path = \
            pathlib.Path(__file__).parent.joinpath('ui-art', 'aibou2.ascii')
    with title_ascii_path.open('r') as file:
        lines = []
        for line in file:
            lines.append(line)
        title = ''.join(lines)
    return title

def make_welcomescreen():
    welcomescreen = WelcomeScreen()
    return welcomescreen

def welcome_text():
    text = 'Welcome to Aibou,'\
    'A turn-based monster battle game.\n'\
    'Press space to begin.'
    return text

def show_title():
    title = make_title()
    text = welcome_text()
    welcomescreen = make_welcomescreen()
    welcomescreen.show(
            Panel(Align(title + '\n' + text,
                        align='center',
                        vertical='middle')
                  )
    )
    welcomescreen.pause(5)

show_title()

