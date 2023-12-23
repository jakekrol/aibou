#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# loads in monster & move data from yaml configs, sets the data dictionary to 
#   a variable accessible to other files via from getdata import VAR_NAME
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# external
import yaml
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\
# std
import pathlib
#\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\

def load_monster_data():
    data_path = pathlib.Path(__file__).parent.parent.parent.joinpath('data/settings')
    monster_data_path = data_path.joinpath('monsters.yaml')
    with monster_data_path.open('r') as file:
       global monster_data
       monster_data = yaml.safe_load(file)
       return monster_data

def load_move_data():
    data_path = pathlib.Path(__file__).parent.parent.parent.joinpath('data/settings')
    move_data_path = data_path.joinpath('moves.yaml')
    with move_data_path.open('r') as file:
        global move_data
        move_data = yaml.safe_load(file)
