#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
import keyboard
import os
from rich.align import Align
from rich.layout import Layout
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich import print
import pathlib
import webbrowser
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
from aibou.ui import screen
from aibou.ui.screen import Screen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
class WelcomeScreen(Screen):

    def __init__(self):
        Screen.__init__(self) 

#def render_monsters(self, partner, boss):
#    # fit monsters in layout height
#    for monster in [partner, boss]:
#        self.fit_monster(monster)
#    self.partner_render = Align(partner.text, align='left', vertical='bottom')
#    self.boss_render = Align(boss.text, align='right', vertical='top')
#    columns = Columns([self.partner_render, self.boss_render], expand=True)
#    self.layout['middle'].update(Panel(columns))
#    return 


def make_title_art():
    title_ascii_path = \
            pathlib.Path(__file__).parent.joinpath('ui-art', 'aibou2.ascii')
    with title_ascii_path.open('r') as file:
        lines = []
        for line in file:
            lines.append(line)
        title_art = ''.join(lines)
    return title_art

def welcome_text():
    description = 'Welcome to Aibou, a turn-based monster battle game.'
    return description

def info_option():
    keyboard.remove_hotkey('i')
    wel('https://github.com/jakekrol/aibou/blob/main/aibou'\
            '/docs/how-to-play.md')

def set_menu_ui(welcomescreen_obj, title_art, description):
    welcomescreen_obj.layout.split_column(
        Layout(name='title', ratio=4),
        Layout(name='options', ratio=6)
    )
    welcomescreen_obj.layout['title'].update(
            Align(title_art + '\n' + description,
                        align='center',
                        vertical='middle'
                 )
             )
    welcomescreen_obj.layout['options'].split_column(
        Layout(name='quickplay'),
        Layout(name='story'),
        Layout(name='settings'),
        Layout(name='info')
    )
    #
    def set_menu_option(layout_name, key, option):
        welcomescreen_obj.layout[layout_name].update(
            Align(
                Text.assemble((key, 'bold'), (f' -> {option}')),
                align='center',
                vertical='middle'
                )
        )
    set_menu_option('quickplay', 'q', 'Quickplay')
    set_menu_option('story', 's', 'Story')
    set_menu_option('settings', 'o', 'Options')
    set_menu_option('info', 'i', 'Info')
    keyboard.add_hotkey('i', callback=info_option)

def show_title():
    title_art = make_title_art()
    description = welcome_text()
    welcomescreen = WelcomeScreen()
    set_menu_ui(welcomescreen, title_art, description)
    welcomescreen.show()
    #choose_partner()
    keyboard.wait('q')
    
#def make_welcomescreen():
#    welcomescreen = WelcomeScreen()
#    return welcomescreen


#def choose_partner():
#    art_path = pathlib.Path(__file__).parent.parent.joinpath('monster-art')
#    partners = os.listdir(art_path)

