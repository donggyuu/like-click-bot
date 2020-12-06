import yaml

# get account config
with open(r'/Users/don/Dropbox/git/temp-click-bot/config.yml') as file:
    documents = yaml.full_load(file)

    for key, value in documents.items():
        if key == 'id':
            id = value
        elif key == 'pw':
            pw = value


        
