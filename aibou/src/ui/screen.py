#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external packages
from rich import print
from rich.layout import Layout
from time import sleep
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
class Screen():
    ''' 
    The parent class for all UIs/Screens. An instance initializes a rich Layout.
    '''

    def __init__(self):
        self.layout = Layout()

    def show(self):
        print(self.layout)

    def pause(self, seconds):
        sleep(seconds)

class Menu(Screen):
    pass

