#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
import keyboard
from rich.align import Align
from rich.layout import Layout
from rich.text import Text
import pathlib
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# local
from aibou.ui.screen import Screen
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

home_art_path = pathlib.Path(__file__).parent.joinpath('ui-art/home')

class HomeScreen(Screen):

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


def load_art(filename):
    art_path = home_art_path.joinpath(filename)
    with art_path.open('r') as file:
        lines = []
        for line in file:
            lines.append(line)
        art = ''.join(lines)
    return art

def welcome_text():
    description = Text('Welcome to Aibou, a turn-based monster battle game.\n' \
            "For optimal experience, expand terminal to max window size.")
    return description

def info_option(key):
    keyboard.remove_hotkey(key)
    # open doc or show text desc

def story_option(key):
    keyboard.remove_hotkey(key)
    # enter story mode

def quickplay_option(key):
    keyboard.remove_hotkey(key)
    # enter quick play

def config_option(key):
    keyboard.remove_hotkey(key)
    # enter quick play

def set_menu_option(layout_name, option):
    homescreen.layout[layout_name].update(
        Align(
            # babyblue: https://www.canva.com/colors/color-palettes/mermaid-lagoon/
            Text(option, '#B1D4E0'),
            align='center',
            vertical='middle'
            )
    )

def set_menu_ui(title_art, description):
    homescreen.layout.split_column(
        Layout(name='title', ratio=30),
        Layout(name='options', ratio=65),
        Layout(name='creator', ratio=5)
    )
    homescreen.layout['title'].update(
            Align(title_art + '\n' + description,
                        align='center',
                        vertical='middle'
                 )
             )
    homescreen.layout['options'].split_column(
        Layout(name='quickplay'),
        Layout(name='story'),
        Layout(name='config'),
        Layout(name='info')
    )
    set_menu_option('quickplay', load_art('quickplay.ascii'))
    set_menu_option('story', load_art('story.ascii'))
    set_menu_option('config', load_art('config.ascii'))
    set_menu_option('info', load_art('info.ascii'))
    #keyboard.add_hotkey('q', args='q', callback=info_option)
    keyboard.add_hotkey('i', args='i', callback=info_option)
    keyboard.add_hotkey('c', args='c', callback=info_option)
    keyboard.add_hotkey('o', args='o', callback=info_option)
    homescreen.layout['creator'].update(
            Align(Text('Created by Jake Krol (2023)', '#2E8BC0'),
                  align='center', vertical='middle')
            )
def show_title():
    title_art = Text(load_art('title.ascii'), '#2E8BC0')
    description = welcome_text()
    global homescreen
    homescreen = HomeScreen()
    set_menu_ui(title_art, description)
    homescreen.show()
    #choose_partner()
    keyboard.wait('q')

#def make_welcomescreen():
#    welcomescreen = WelcomeScreen()
#    return welcomescreen


#def choose_partner():
#    art_path = pathlib.Path(__file__).parent.parent.joinpath('monster-art')
#    partners = os.listdir(art_path)
