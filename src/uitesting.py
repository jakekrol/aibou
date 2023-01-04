# coding: utf-8
import rich
from rich import Columns
from rich.columns import Columns
from rich.layout import Layout
from rich import print
from rich.align import Align
from rich.style import Style
layout = Layout()
print(layout)
layout.split_row(
Layout(name='row1'),
Layout(name='row2'))
layout
print(layout)
layout = Layout()
print(layout)
layout.split_column(
Layout(name='upper'),
Layout(name='lower'))
print(layout)
from rich.panel import Panel
style = (color='red', bgcolor='grey', italic=True)
style = Style(color='red', bgcolor='grey', italic=True)
style = Style(color='red', bgcolor='gray', italic=True)
style = Style(color='red', bgcolor='lightgray', italic=True)
style = Style(color='red', bgcolor='white', italic=True)
boss = Style(color='red', bgcolor='white', italic=True)
print('Boss', style=boss)
from rich import print
print('Boss', style=boss)
from rich.text import Text
test = Text('Bossname')
text = Text('Bossname')
text = Text()
text.append('Bossname', style-boss)
text.append('Bossname', style=boss)
