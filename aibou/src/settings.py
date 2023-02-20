import yaml

def set_difficulty(selection):
    # load settings file
    with open('../data/settings.yaml', 'r') as settings_file:
        settings = yaml.safe_load(settings_file)
        difficulty = settings['difficulty']
        # check if current setting is the same as the selection
        if selection == difficulty:
            return
        # update difficulty setting
        settings['difficulty'] = selection
    with open('../data/settings.yaml', 'w') as settings_file:
        # write to file
        yaml.dump(settings, settings_file)

