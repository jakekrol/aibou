import monster

def get_movedata()
def check_kill(partner, boss):
    with open(f'{os.getcwd()}/../data/attacks.yaml', 'r') as file:
        data = yaml.safe_load(file)


    with open(f'{os.getcwd()}/../data/attacks.yaml', 'r') as file:
        data = yaml.safe_load(file)
        power = data[move]['power'] 
        skill = data[move]['skill'] 
        num_events = data[move]['num_events'] 
        event_time = data[move]['event_time'] 

def choose_move():

